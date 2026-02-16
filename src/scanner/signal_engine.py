import pandas as pd
import logging

class SignalEngine:
    """
    SignalEngine scans markets and identifies trading signals based on predefined strategies.
    """

    @staticmethod
    def scan_market(market_data, strategy):
        """
        Analyze market data and identify trading signals based on a strategy.
        Args:
            market_data (pd.DataFrame): Historical market data.
            strategy (callable): Function implementing the trading strategy logic.
        Returns:
            list: Detected trading signals.
        """
        logging.info("Starting market scan with the given strategy.")
        
        if not isinstance(market_data, pd.DataFrame):
            logging.error("Invalid market data format. Expected pandas DataFrame.")
            return []

        try:
            signals = strategy(market_data)
            logging.info(f"Scan complete. Detected {len(signals)} signals.")
            return signals
        except Exception as e:
            logging.error(f"Error during market scan: {e}")
            return []

# Example usage:
def example_strategy(market_data):
    """Example strategy for identifying buy/sell signals."""
    return [
        {
            "symbol": row["symbol"],
            "price": row["close"],
            "time": row["timestamp"],
            "signal_type": "BUY" if row["rsi"] < 30 else "SELL" if row["rsi"] > 70 else "HOLD"
        }
        for _, row in market_data.iterrows()
    ]