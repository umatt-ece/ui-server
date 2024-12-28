from typing import Union

from fastapi import FastAPI, APIRouter
from fastapi_utils.cbv import cbv

from common import ParameterStore, VARIABLES

router = APIRouter()

@cbv(router)
class ItemView:
    def __init__(self):
        pass
    
    @router.get("/")
    def read_root(self):
        return {"Hello": "World"}

    @router.get("/data")
    def get_data(self):
        ps = ParameterStore()
        data = {}
        for key, value in VARIABLES.items():
            data[key] = ps.get(key)
        return data

    # @router.get("/frontend")
    # def frontend_static_files():
    #     pass
        # files = StaticFiles("index.html")
        # return files



    @router.get("/test_bool/{key}/{value}")
    def read_item(self,key: str, value: bool):
        ps = ParameterStore()
        ps.set(key, value)

    # todo: websockets...
    

