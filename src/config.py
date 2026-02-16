"""
import os
from dotenv import load_dotenv

class Config:
    """Load configuration settings from .env file."""

    def __init__(self):
        load_dotenv()
        self.db_path = os.getenv("DB_PATH", "trade_memory.db")
        self.dry_run = os.getenv("DRY_RUN", "true").lower() == "true"
        self.api_key = os.getenv("API_KEY")
        self.api_secret = os.getenv("API_SECRET")
        self.risk_parameters = {
            "risk_per_trade": float(os.getenv("RISK_PER_TRADE", 0.0025)),
            "daily_loss_limit": float(os.getenv("DAILY_LOSS_LIMIT", 0.02)),
            "max_positions": int(os.getenv("MAX_POSITIONS", 2)),
            "cooldown_minutes": int(os.getenv("COOLDOWN_MINUTES", 60)),
            "leverage_cap": float(os.getenv("LEVERAGE_CAP", 10.0)),
        }
"""