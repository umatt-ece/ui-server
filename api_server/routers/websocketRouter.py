from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from common.redis_helper import ParameterStore  # Import your ParameterStore

ws_router = APIRouter()
parameter_store = ParameterStore()  # Initialize the ParameterStore

@ws_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # Receive JSON data from the WebSocket
            data = await websocket.receive_json()

            # Extract command and arguments
            command = data.get("command")
            key = data.get("key")
            value = data.get("value")
            keys = data.get("keys")
            
            response = {}
            try:
                if command == "set" and key and value is not None:        # If the user want to set value
                    parameter_store.set(key, value)
                    response = {"status": "success", "message": f"Key '{key}' set successfully."}

                elif command == "get" and key:                              # If the user want to get value
                    value = parameter_store.get(key)
                    response = {"status": "success", "key": key, "value": value}

                elif command == "mset" and isinstance(value, dict):
                    parameter_store.mset(value)
                    response = {"status": "success", "message": "Keys set successfully."}

                elif command == "mget" and isinstance(keys, list):
                    values = parameter_store.mget(keys)
                    response = {"status": "success", "values": values}

                else:
                    response = {"status": "error", "message": "Invalid command or missing arguments."}

            except Exception as e:
                response = {"status": "error", "message": str(e)}

            # Send the response back through the WebSocket
            await websocket.send_json(response)

    except WebSocketDisconnect:
        print("WebSocket disconnected")
        
'''
    Message sent from the user should be in format:
    {
    "command": "set",
    "key": "this_is_key",
    "value": "Hello, world!"
    }
'''
