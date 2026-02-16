import sqlite3
import pandas as pd
import json
import os
from datetime import datetime

# Database connection
DB_PATH = 'trade_memory.db'

# Configurable parameters
N = 50

# Function to connect to the SQLite database and pull trades

def get_last_n_trades(n):
    try:
        conn = sqlite3.connect(DB_PATH)
        query = f'SELECT * FROM trades ORDER BY timestamp DESC LIMIT {n}'
        trades_df = pd.read_sql_query(query, conn)
        return trades_df
    except Exception as e:
        print(f'Error fetching trades: {e}')
        return pd.DataFrame()  # Return empty DataFrame on failure
    finally:
        if conn:
            conn.close()

# Function to compute metrics from trades DataFrame

def compute_metrics(trades_df):
    total_trades = len(trades_df)
    if total_trades == 0:
        return None  # No trades to compute
    winrate = (trades_df['result'] > 0).mean()
    average_r_multiple = trades_df['r_multiple'].mean()
    average_duration_minutes = trades_df['duration'].mean() / 60  # Duration in seconds to minutes

    # Group metrics by regime
    regime_breakdown = trades_df.groupby('regime')['result'].mean().to_dict()
    # Group metrics by setup type
    setup_breakdown = trades_df.groupby('setup_type')['result'].mean().to_dict()

    # Group by RSI buckets
    trades_df['rsi_bucket'] = pd.cut(trades_df['rsi'], bins=[-float('inf'), 30, 50, 70, float('inf')], labels=['< 30', '30-50', '50-70', '> 70'])
    rsi_bucket_performance = trades_df.groupby('rsi_bucket')['result'].mean().to_dict()

    # Calculate maximum drawdown
    max_drawdown = (trades_df['drawdown'].min() if 'drawdown' in trades_df.columns else float('nan'))

    return {
        "total_trades": total_trades,
        "winrate": winrate,
        "avg_r": average_r_multiple,
        "regime_breakdown": regime_breakdown,
        "setup_breakdown": setup_breakdown,
        "rsi_bucket_performance": rsi_bucket_performance,
        "max_drawdown": max_drawdown
    }

# Generate a JSON summary and save it

def save_summary_to_file(summary):
    date_str = datetime.utcnow().strftime('%Y-%m-%d')
    file_path = f'reports/nightly_summary_{date_str}.json'
    try:
        with open(file_path, 'w') as json_file:
            json.dump(summary, json_file, indent=4)
        print(f'Summary saved to {file_path}')
    except Exception as e:
        print(f'Error writing summary to file: {e}')

# Function to generate LLM prompt

def generate_llm_prompt(summary_json):
    return f"Here is the summary of the last trades: {json.dumps(summary_json, indent=4)}"

# Main execution
if __name__ == '__main__':
    trades = get_last_n_trades(N)
    metrics = compute_metrics(trades)
    if metrics:
        print(metrics)
        save_summary_to_file(metrics)