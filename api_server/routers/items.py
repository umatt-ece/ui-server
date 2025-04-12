# ===========================================================
# items.py - FastAPI HTTP routes using class-based views (CBV)
#
# This module defines basic API endpoints for testing and
# interacting with Redis-stored parameters through HTTP.
#
# It uses FastAPI's class-based view (@cbv) pattern, with
# endpoints mounted on a shared router instance.
# ===========================================================

from typing import Union

from fastapi import FastAPI, APIRouter
from fastapi_utils.cbv import cbv

from common import ParameterStore, VARIABLES  # Import parameter store and parameter metadata

# -----------------------------------------------------------
# Initialize API router for this group of endpoints
# -----------------------------------------------------------
router = APIRouter()

# ===========================================================
# Class-Based View: ItemView
#
# Purpose:
#   Encapsulates all API routes related to testing or retrieving
#   parameter values via HTTP GET requests.
#
# Notes:
#   - Uses FastAPI Utilities' @cbv decorator for cleaner structure
# ===========================================================
@cbv(router)
class ItemView:
    def __init__(self):
        # Constructor (currently unused)
        pass

    # -------------------------------------------------------
    # Route: GET /
    # Purpose:
    #   Basic root route to verify the API is up
    # Response:
    #   {"Hello": "World"}
    # -------------------------------------------------------
    @router.get("/")
    def read_root(self):
        return {"Hello": "World"}

    # -------------------------------------------------------
    # Route: GET /data
    # Purpose:
    #   Retrieve the current value for all known VARIABLES
    # Returns:
    #   Dictionary mapping each key to its current value in Redis
    # -------------------------------------------------------
    @router.get("/data")
    def get_data(self):
        ps = ParameterStore()
        data = {}
        for key, value in VARIABLES.items():
            data[key] = ps.get(key)
        return data

    # -------------------------------------------------------
    # Route: GET /test_bool/{key}/{value}
    # Purpose:
    #   A simple endpoint to test boolean set operations.
    #   Sets the given Redis key to the specified boolean value.
    # Parameters:
    #   - key (str): Redis key
    #   - value (bool): Value to store
    # Returns:
    #   None (implicit 200 OK)
    # -------------------------------------------------------
    @router.get("/test_bool/{key}/{value}")
    def read_item(self, key: str, value: bool):
        ps = ParameterStore()
        ps.set(key, value)

    # -------------------------------------------------------
    # (Commented Out) Placeholder for serving frontend UI
    # @router.get("/frontend")
    # def frontend_static_files():
    #     files = StaticFiles("index.html")
    #     return files
    # -------------------------------------------------------

    # -------------------------------------------------------
    # TODO:
    #   Add WebSocket-based communication if needed
    #   to mirror what's available in websocketrouter.py
    # -------------------------------------------------------
