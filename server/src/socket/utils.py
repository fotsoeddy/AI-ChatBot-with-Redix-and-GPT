from fastapi import WebSocket, status, Query
from fastapi.exceptions import HTTPException
from typing import Optional

async def get_token(
    websocket: WebSocket,
    token: Optional[str] = Query(None),
):
    if token is None or token == "":
        raise HTTPException(
            status_code=status.WS_1008_POLICY_VIOLATION,
            detail="Token is missing or invalid"
        )
    return token