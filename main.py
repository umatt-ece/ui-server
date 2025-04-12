# ===========================================================
# main.py - FastAPI Application Entry Point
#
# This file serves as the startup script for the API server.
# It sets up route mounting, static file serving, and template
# rendering using Jinja2. It also integrates WebSocket support.
#
# Run this file directly to launch the development server:
#   python api_server/main.py
# ===========================================================

from typing import Union

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from api_server.routers import items_router             # (Optional) Import for HTTP route group
from api_server.routers.websocketRouter import ws_router  # Import WebSocket route
import threading
import time
import uvicorn

# -----------------------------------------------------------
# Initialize the FastAPI application
# -----------------------------------------------------------
app = FastAPI()

from common.redis_helper import ParameterStore  # Redis interface (can be used by routes)

# -----------------------------------------------------------
# Configure Jinja2 for rendering HTML templates
# Directory: api_server/templates
# -----------------------------------------------------------
templates = Jinja2Templates(directory="api_server/templates")

# -----------------------------------------------------------
# Serve static files (e.g., JS, CSS, images) under /static
# Directory: api_server/static
# -----------------------------------------------------------
app.mount("/static", StaticFiles(directory="api_server/static"), name="static")

# -----------------------------------------------------------
# Route: GET /
# Purpose:
#   Serve the main frontend (index.html) using Jinja2
# -----------------------------------------------------------
@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# -----------------------------------------------------------
# Include route groups
# Note:
#   items_router is currently commented out
#   ws_router handles WebSocket communication at /ws
# -----------------------------------------------------------
# app.include_router(items_router)
app.include_router(ws_router)  # Enable WebSocket route

# -----------------------------------------------------------
# Server entry point
# Purpose:
#   Run the FastAPI server with Uvicorn when executed directly
#   Enables hot reload for development
# -----------------------------------------------------------
if __name__ == "__main__":
    uvicorn.run("api_server.main:app", host="0.0.0.0", port=8000, reload=True)
