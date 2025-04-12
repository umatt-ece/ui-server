# ===========================================================
# websocketrouter.py - WebSocket endpoint for parameter control
#
# This module defines a FastAPI WebSocket route at `/ws` that allows
# clients to send commands for setting and retrieving parameters
# stored in Redis via the ParameterStore abstraction.
#
# Supported Commands via WebSocket JSON messages:
#   - "set"   : set a single key-value pair
#   - "get"   : get the value of a specific key
#   - "mset"  : set multiple key-value pairs (dictionary)
#   - "mget"  : get multiple key-value pairs (list of keys)
#
# Usage:
#   Send JSON messages through WebSocket to control parameters.
# ===========================================================

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from common.redis_helper import ParameterStore  # Import your ParameterStore

# -------------------------------------------
# Initialize WebSocket router and Redis store
# -------------------------------------------
ws_router = APIRouter()
parameter_store = ParameterStore()  # Initialize the ParameterStore

# ===========================================================
# WebSocket Endpoint: /ws
#
# Purpose:
#   Accepts and processes real-time JSON commands for parameter
#   manipulation via WebSocket. Supports bidirectional communication.
#
# Parameters:
#   - websocket (WebSocket): Incoming WebSocket connection from client
#
# Accepted JSON format from client:
#   {
#     "command": "set" | "get" | "mset" | "mget",
#     "key": <str>,            # Optional, used in "get" or "set"
#     "value": <Any>,          # Optional, used in "set" or "mset"
#     "keys": <List[str]>      # Optional, used in "mget"
#   }
#
# Example:
#   {"command": "set", "key": "GEAR", "value": 2}
# ===========================================================
@ws_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()  # Accept the WebSocket connection
    try:
        while True:
            # --------------------------------------------------
            # Receive and parse JSON message from the WebSocket
            # --------------------------------------------------
            data = await websocket.receive_json()

            # Extract command and arguments
            command = data.get("command")
            key = data.get("key")
            value = data.get("value")
            keys = data.get("keys")
            
            response = {}

            # --------------------------------------------------
            # Handle command and interact with ParameterStore
            # --------------------------------------------------
            try:
                if command == "set" and key and value is not None:  # Set a single key-value pair
                    parameter_store.set(key, value)
                    response = {"status": "success", "message": f"Key '{key}' set successfully."}

                elif command == "get" and key:  # Retrieve a single key's value
                    value = parameter_store.get(key)
                    response = {"status": "success", "key": key, "value": value}

                elif command == "mset" and isinstance(value, dict):  # Set multiple key-value pairs
                    parameter_store.mset(value)
                    response = {"status": "success", "message": "Keys set successfully."}

                elif command == "mget" and isinstance(keys, list):  # Get multiple keys
                    values = parameter_store.mget(keys)
                    response = {"status": "success", "values": values}

                else:
                    # Invalid or missing fields
                    response = {"status": "error", "message": "Invalid command or missing arguments."}

            except Exception as e:
                # Handle Redis or data errors
                response = {"status": "error", "message": str(e)}

            # --------------------------------------------------
            # Send the result back to the WebSocket client
            # --------------------------------------------------
            await websocket.send_json(response)

    except WebSocketDisconnect:
        # Handle disconnection cleanly
        print("WebSocket disconnected")


'''
    🔧 Example usage format (JSON message to send via WebSocket):

    {
        "command": "set",
        "key": "this_is_key",
        "value": "Hello, world!"
    }
'''
