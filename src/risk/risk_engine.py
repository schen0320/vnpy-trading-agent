import logging

class RiskEngine:
    risk_percent = 0.25
    daily_loss_cap = 2.0
    max_concurrent_positions = 2
    current_concurrent_positions = 0
    daily_loss = 0.0

    @staticmethod
    def initialize(risk_percent, loss_cap, concurrent_positions):
        RiskEngine.risk_percent = risk_percent
        RiskEngine.daily_loss_cap = loss_cap
        RiskEngine.max_concurrent_positions = concurrent_positions
        logging.info("RiskEngine initialized with parameters. Risk: %.2f%%, Loss Cap: %.2f%%, Max Positions: %d",
                     risk_percent, loss_cap, concurrent_positions)

    @staticmethod
    def evaluate_signal(signal):
        """
        Evaluate signals for risk compliance.
        Returns a validated TradeIntent object if risk conditions are met, otherwise None.
        """
        if RiskEngine.current_concurrent_positions >= RiskEngine.max_concurrent_positions:
            logging.warning("Risk denied: Too many concurrent positions.")
            return None

        if RiskEngine.daily_loss >= RiskEngine.daily_loss_cap:
            logging.warning("Risk denied: Daily loss cap reached.")
            return None

        if signal["rsi"] > 72 and signal["signal_type"] == "LONG" and signal["confirmation"] != "retest":
            logging.warning("Risk denied: RSI > 72 for LONG.")
            return None

        if signal["rsi"] < 28 and signal["signal_type"] == "SHORT" and signal["confirmation"] != "retest":
            logging.warning("Risk denied: RSI < 28 for SHORT.")
            return None

        if signal["symbol"] and signal["signal_type"]:
            # Assuming a dummy TradeIntent object
            return {
                "symbol": signal["symbol"],
                "action": signal["signal_type"],
                "risk": RiskEngine.risk_percent
            }

        logging.warning("Risk denied: Invalid signal.")
        return None