import redis.asyncio as redis
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Redis:
    def __init__(self):
        """Initialize connection."""
        # Hardcoded local Redis connection details
        self.REDIS_URL = "localhost:6379"  # Local Redis server
        self.REDIS_PASSWORD = ""           # No password for local Redis
        self.REDIS_USER = "default"        # Default user for local Redis
        
        # Log the connection details for debugging
        logger.info(f"REDIS_URL: {self.REDIS_URL}")
        logger.info(f"REDIS_USER: {self.REDIS_USER}")
        logger.info(f"REDIS_PASSWORD: {self.REDIS_PASSWORD}")

        # Construct the Redis connection URL
        if self.REDIS_PASSWORD:
            self.connection_url = f"redis://{self.REDIS_USER}:{self.REDIS_PASSWORD}@{self.REDIS_URL}"
        else:
            self.connection_url = f"redis://{self.REDIS_URL}"

        logger.info(f"Connecting to Redis at {self.connection_url}")

    async def create_connection(self):
        """Create and return a Redis connection."""
        try:
            self.connection = redis.from_url(
                self.connection_url, db=0
            )
            logger.info("Redis connection established successfully!")
            return self.connection
        except Exception as e:
            logger.error(f"Failed to connect to Redis: {e}")
            raise