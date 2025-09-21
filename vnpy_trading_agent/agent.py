import logging

from .config import AppConfig


class TradingAgent:
    """Skeleton trading agent.

    Wire this up to vn.py engines/gateways as you build out functionality.
    """

    def __init__(self, config: AppConfig) -> None:
        self.config = config
        self.logger = logging.getLogger("vnpy_trading_agent")

    def run(self) -> None:
        """Entry point for starting the agent runtime."""

        self.logger.info("Starting vn.py trading agent")
        self.logger.info("Log level: %s", self.config.log_level)

        if self.config.strategy_name:
            self.logger.info("Strategy: %s", self.config.strategy_name)
        if self.config.vt_symbol:
            self.logger.info("Symbol: %s", self.config.vt_symbol)
        if self.config.config_path:
            self.logger.info("Config file: %s", self.config.config_path)

        # TODO: Initialize vn.py engines, connect to gateway, and load strategy.
        # This template logs startup information as a placeholder.
        self.logger.info("Agent initialized. Implement vn.py engine startup here.")
