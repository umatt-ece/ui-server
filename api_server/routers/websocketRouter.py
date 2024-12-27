from fastapi import FastAPI, WebSocket, APIRouter
from fastapi.responses import HTMLResponse
from fastapi_utils.cbv import cbv

router = APIRouter()

class WebSocketView:
    def __init__(self):
        pass
    
    async def websocket_endpoint(self,websocket: WebSocket):
        await websocket.accept()
        
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(data)

# Create an instance of the class
websocket_view = WebSocketView()

# Register the WebSocket route manually
router.add_api_websocket_route("/ws", websocket_view.websocket_endpoint)