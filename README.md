# vnpy-trading-agent

The `vnpy-trading-agent` is a risk-first automated trading system designed for crypto markets and operating seamlessly with exchanges like OKX and HyperLiquid.

## Features
- Risk-first trading architecture emphasizing safety and consistent returns.
- Modular design with core components:
  - **Risk Engine**: Evaluates and enforces risk rules.
  - **Decision Router**: Routes validated trade intents.
  - **Execution Layer**: Includes integrations for OKX and HyperLiquid.
- SQLite database support for persisting trades, decisions, and signals.
- Performance reporting with comprehensive metrics.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/schen0320/vnpy-trading-agent.git
   cd vnpy-trading-agent
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv env
   source env/bin/activate  # For Windows use `env\Scripts\activate`
   pip install -r requirements.txt
   ```
3. Initialize the database:
   ```bash
   python scripts/init_db.py
   ```

## Scripts
### `scripts/init_db.py`
Initialize the SQLite database (`trade_memory.db`) with tables for storing trades, signals, decisions, and other necessary data.

### `scripts/nightly_review.py`
1. Connects to the SQLite database to pull the last 50 (configurable) trades.
2. Computes detailed performance metrics including win rate, R-multiples, trade duration, and more.
3. Produces a JSON summary with the calculated metrics.
4. Saves the summary in a timestamped JSON file in the `reports/` directory.
5. Prints a readable summary to the console.
6. Includes a function to generate structured messages for an optional manual review using an LLM.

Run the script as follows:
```bash
python scripts/nightly_review.py
```

## Development
- Ensure to write tests for any new functionality.
- Provide meaningful commit messages and adhere to coding best practices.

## Contributions
Contributions are welcome! To contribute:
- Fork the repository
- Create a new branch for your feature or bugfix
- Open a Pull Request with a clear description