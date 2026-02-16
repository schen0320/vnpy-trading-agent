from dotenv import load_dotenv
import os

class Config:
    # Default Configuration Variables
    RISK_PCT = 0.25  # max risk percentage per trade
    DAILY_LOSS_CAP = 2.0  # max daily loss cap in percentage
    MAX_CONCURRENT_POSITIONS = 2
    DB_PATH = "trade_memory.db"
    ENV_FILE = ".env"

    @staticmethod
    def load_environment():
        """Load environment variables from .env file."""
        if os.path.exists(Config.ENV_FILE):
            load_dotenv(Config.ENV_FILE)