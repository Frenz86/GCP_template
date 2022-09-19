from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn
import os 

app = FastAPI(title="API1", description="with FastAPI by Daniele Grotti", version="1.0")
templates = Jinja2Templates(directory="templates")




@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run("main:app",host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))