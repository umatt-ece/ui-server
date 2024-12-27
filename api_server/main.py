from typing import Union

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from api_server.routers import items_router
from api_server.routers import ws_router
import threading
import time

app = FastAPI()

templates = Jinja2Templates(directory="api_server/templates")

app.mount("/static", StaticFiles(directory="api_server/static"),name ="static")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})

class BackGroundTask(threading.Thread):
    while True:
        print("Hello")
        time.sleep(5)
        
thread = threading.Thread(target=BackGroundTask, daemon= True)

app.include_router(items_router)
app.include_router(ws_router)