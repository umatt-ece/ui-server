from typing import Union

from fastapi import FastAPI

from common import VARIABLES, ParameterStore

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/data")
def get_data():
    ps = ParameterStore()
    data = {}
    for key, value in VARIABLES.items():
        data[key] = ps.get(key)
    return data


@app.get("/test_bool/{value}")
def read_item(key: str, value: bool):
    ps = ParameterStore()
    ps.set(key, value)

# todo: websockets...