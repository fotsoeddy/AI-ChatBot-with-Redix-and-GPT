from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Request, Depends, HTTPException
import uuid
from ..socket.connection import ConnectionManager
from ..socket.utils import get_token
from ..redis.producer import Producer
from ..redis.config import Redis

chat = APIRouter()
manager = ConnectionManager()
redis = Redis()

# Endpoint to generate a token
@chat.post("/token")
async def token_generator(name: str, request: Request):
    token = str(uuid.uuid4())

    if name == "":
        raise HTTPException(status_code=400, detail={
            "loc": "name",  "msg": "Enter a valid name"
        })

    data = {"name": name, "token": token}
    return data

# WebSocket endpoint for chat
@chat.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket, token: str = Depends(get_token)):
    await manager.connect(websocket)
    redis_client = await redis.create_connection()
    producer = Producer(redis_client)

    try:
        while True:
            data = await websocket.receive_text()
            print(data)
            stream_data = {token: data}
            await producer.add_to_stream(stream_data, "message_channel")
            await manager.send_personal_message(f"Response: Simulating response from the GPT service", websocket)

    except WebSocketDisconnect:
        manager.disconnect(websocket)