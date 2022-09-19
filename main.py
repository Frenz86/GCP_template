from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import StreamingResponse
import uvicorn
import os 

app = FastAPI(title="API1", description="with FastAPI by Daniele Grotti", version="1.0")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/get")
def read_root():
    return {"Hello": "World"}


@app.get("/plot")
def loadplot():
    file = open('dog.jpg', mode="rb")
    return StreamingResponse(file, media_type="image/png")

@app.get("/predict")
def precit():
    return {"classe": "iris"} 

@app.post("/predict")
def precit():
    return {"classe": "iris"} 

if __name__ == "__main__":
    uvicorn.run("main:app",host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))