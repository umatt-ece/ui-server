from typing import Union

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from api_server.routers import items_router
from api_server.routers.websocketRouter import ws_router
import threading
import time
import uvicorn

app = FastAPI()
from common.redis_helper import ParameterStore

templates = Jinja2Templates(directory="api_server/templates")

app.mount("/static", StaticFiles(directory="api_server/static"),name ="static")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})

#app.include_router(items_router)
app.include_router(ws_router)  # this will try the websocket connection

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)