import os
from dotenv import load_dotenv
import aioredis

load_dotenv()

class Redis():
    def __init__(self):
        """initialize  connection """
        self.REDIS_URL = os.environ['REDIS_URL']
        self.REDIS_PASSWORD = os.environ['REDIS_PASSWORD']
        self.REDIS_USER = os.environ['REDIS_USER']
        self.connection_url = f"redis://{self.REDIS_USER}:{self.REDIS_PASSWORD}@{self.REDIS_URL}"

    async def create_connection(self):
        self.connection = aioredis.from_url(
            self.connection_url, db=0)

        return self.connection

from worker.redis.config import Redis
import asyncio

async def main():
    redis = Redis()
    redis = await redis.create_connection()
    print(redis)
    await redis.set("key", "value")

if __name__ == "__main__":
    asyncio.run(main())