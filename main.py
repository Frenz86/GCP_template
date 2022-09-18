from fastapi import FastAPI, Request,Depends,HTTPException
from fastapi.responses import StreamingResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.responses import JSONResponse
import pandas as pd
import uvicorn
from pydantic import BaseModel
import joblib
import os 

import warnings
warnings.filterwarnings("ignore")

classes = {
    0: 'setosa',
    1: 'versicolor',
    2: 'virginica'
}

class Feature_type(BaseModel):
    #description: Optional[str] = None questo è un campo opzionale
    feature1 : float = 3.0
    feature2 : float = 3.0
    feature3 : float = 3.0
    feature4 : float = 3.0

app = FastAPI(title="API1", description="with FastAPI by Daniele Grotti", version="1.0")
templates = Jinja2Templates(directory="templates")

@app.on_event("startup") #define event handlers (functions) that need to be executed before the application starts up
def load_model():
    global model
    model = joblib.load("iris.pkl")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



@app.get("/predict", response_class=HTMLResponse)
async def predict_get(data: Feature_type= Depends()):              # depends() input nelle celle
    try:
        data = pd.DataFrame(data)
        data = data.T
        data.rename(columns=data.iloc[0], inplace = True)
        data= data.iloc[1:] #must have array
        
        y_pred = list(map(lambda x: classes[x], model.predict(data).tolist()))[0]
        return JSONResponse(y_pred)
    except:
        raise HTTPException(status_code=404, detail="error")

# @app.post("/predict", response_class=HTMLResponse)
# #async def predict_post(data: Feature_type= Depends()):
# async def predict_post(data: Feature_type):
#     try:
#         data = pd.DataFrame(data).T
#         data.rename(columns=data.iloc[0], inplace = True)
#         data= data.iloc[1:] #must have array
#         y_pred = list(map(lambda x: classes[x], model.predict(data).tolist()))[0]
#         return JSONResponse(y_pred)
#     except:
#         raise HTTPException(status_code=404, detail="error") 

# @app.get("/predict", response_class=HTMLResponse)
# async def predict_get(data: Feature_type= Depends()):              # depends() input nelle celle
#     try:
#         data = pd.DataFrame(data)
#         data = data.T
#         data.rename(columns=data.iloc[0], inplace = True)
#         data= data.iloc[1:] #must have array
        
#         y_pred = list(map(lambda x: classes[x], model.predict(data).tolist()))[0]
#         return JSONResponse(y_pred)
#     except:
#         raise HTTPException(status_code=404, detail="error")

# @app.post("/predict", response_class=HTMLResponse)
# #async def predict_post(data: Feature_type= Depends()):
# async def predict_post(data: Feature_type):
#     try:
#         data = pd.DataFrame(data).T
#         data.rename(columns=data.iloc[0], inplace = True)
#         data= data.iloc[1:] #must have array
#         y_pred = list(map(lambda x: classes[x], model.predict(data).tolist()))[0]
#         return JSONResponse(y_pred)
#     except:
#         raise HTTPException(status_code=404, detail="error") 

# @app.get("/pcaplot")
# def get_iris():
#     import matplotlib.pyplot as plt
#     from mpl_toolkits.mplot3d import Axes3D
#     from sklearn import datasets
#     from sklearn.decomposition import PCA

#     # import some data to play with
#     iris = datasets.load_iris()
#     X = iris.data[:, :2]  # we only take the first two features.
#     y = iris.target

#     x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
#     y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5

#     plt.figure(2, figsize=(8, 6))
#     plt.clf()

#     # Plot the training points
#     plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1, edgecolor="k")
#     plt.xlabel("Sepal length")
#     plt.ylabel("Sepal width")

#     plt.xlim(x_min, x_max)
#     plt.ylim(y_min, y_max)
#     plt.xticks(())
#     plt.yticks(())
#     plt.title("Iris PCA Plot")

#     # To getter a better understanding of interaction of the dimensions
#     # plot the first three PCA dimensions
#     fig = plt.figure(1, figsize=(8, 6))
#     ax = Axes3D(fig, elev=-150, azim=110)
#     X_reduced = PCA(n_components=3).fit_transform(iris.data)
#     ax.scatter(
#         X_reduced[:, 0],
#         X_reduced[:, 1],
#         X_reduced[:, 2],
#         c=y,
#         cmap=plt.cm.Set1,
#         edgecolor="k",
#         s=40,
#     )
#     ax.set_title("First three PCA directions")
#     ax.set_xlabel("1st eigenvector")
#     ax.w_xaxis.set_ticklabels([])
#     ax.set_ylabel("2nd eigenvector")
#     ax.w_yaxis.set_ticklabels([])
#     ax.set_zlabel("3rd eigenvector")
#     ax.w_zaxis.set_ticklabels([])

#     fig.savefig('iris.png')
#     file = open('iris.png', mode="rb")
#     return StreamingResponse(file, media_type="image/png")



if __name__ == "__main__":
    uvicorn.run("main:app",host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))