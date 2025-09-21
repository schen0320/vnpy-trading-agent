# vnpy-trading-agent

Minimal vn.py-based trading agent scaffold.

## Quickstart

1. Create and activate a virtual environment
   - python -m venv .venv
   - source .venv/bin/activate

2. Install dependencies
   - pip install -r requirements.txt

3. Run the agent (prints startup info)
   - python -m vnpy_trading_agent --log-level DEBUG

4. Optional: use a YAML config
   - Save a file `config.yaml` like:
     ```yaml
     log_level: INFO
     strategy_name: SampleStrategy
     vt_symbol: AAPL.USD
     ```
   - python -m vnpy_trading_agent -c config.yaml

Environment variables can also override settings:
- VNTA_CONFIG: path to config file
- VNTA_LOG_LEVEL: log level (e.g. DEBUG)
- VNTA_STRATEGY_NAME: strategy name
- VNTA_VT_SYMBOL: vt symbol

## Notes

This is a skeleton. Wire up vn.py engines/gateways and strategy loading in `vnpy_trading_agent/agent.py`.
