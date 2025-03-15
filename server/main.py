from fastapi import FastAPI, Request
import uvicorn
import os
from dotenv import load_dotenv
from src.routes.chat import chat
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()  # Load environment variables from .env file

# Log environment variables for debugging
logger.info(f"APP_ENV: {os.getenv('APP_ENV')}")
logger.info(f"REDIS_URL: {os.getenv('REDIS_URL')}")
logger.info(f"REDIS_USER: {os.getenv('REDIS_USER')}")
logger.info(f"REDIS_PASSWORD: {os.getenv('REDIS_PASSWORD')}")
logger.info(f"REDIS_HOST: {os.getenv('REDIS_HOST')}")
logger.info(f"REDIS_PORT: {os.getenv('REDIS_PORT')}")

api = FastAPI()
api.include_router(chat)

@api.get("/test")
async def root():
    return {"msg": "API is Online"}

if __name__ == "__main__":
    if os.environ.get('APP_ENV') == "development":
        uvicorn.run("main:api", host="0.0.0.0", port=3500,
                    workers=4, reload=True)
    else:
        pass