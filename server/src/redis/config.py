import redis.asyncio as redis
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import redis.asyncio as redis
from redis import Redis as Client  # For ReJSON

class Redis:
    def __init__(self):
        """Initialize connection."""
        # Hardcoded local Redis connection details
        self.REDIS_URL = "localhost:6379"  # Local Redis server
        self.REDIS_PASSWORD = ""           # No password for local Redis
        self.REDIS_USER = "default"        # Default user for local Redis
        self.REDIS_HOST = "localhost"      # Local Redis host
        self.REDIS_PORT = 6379             # Local Redis port

        # Construct the Redis connection URL
        if self.REDIS_PASSWORD:
            self.connection_url = f"redis://{self.REDIS_USER}:{self.REDIS_PASSWORD}@{self.REDIS_URL}"
        else:
            self.connection_url = f"redis://{self.REDIS_URL}"

    async def create_connection(self):
        """Create and return an async Redis connection."""
        self.connection = redis.from_url(
            self.connection_url, db=0
        )
        return self.connection

    def create_rejson_connection(self):
        """Create and return a Redis connection for ReJSON."""
        self.redisJson = Client(
            host=self.REDIS_HOST,
            port=self.REDIS_PORT,
            decode_responses=True,
            username=self.REDIS_USER,
            password=self.REDIS_PASSWORD
        )
        return self.redisJson