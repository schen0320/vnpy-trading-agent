import argparse
import sys
from typing import Optional

from .agent import TradingAgent
from .config import AppConfig, apply_overrides_from_cli, load_config
from .logging_config import setup_logging


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="vnpy-trading-agent",
        description="Run the vn.py-based trading agent",
    )
    parser.add_argument(
        "-c",
        "--config",
        help="Path to YAML config file",
        default=None,
    )
    parser.add_argument(
        "-l",
        "--log-level",
        help="Override log level (DEBUG, INFO, WARNING, ERROR)",
        default=None,
    )
    return parser


def main(argv: Optional[list[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    config: AppConfig = load_config(args.config)
    config = apply_overrides_from_cli(config, log_level=args.log_level)

    setup_logging(config.log_level)

    agent = TradingAgent(config)
    agent.run()

    return 0


if __name__ == "__main__":
    sys.exit(main())
