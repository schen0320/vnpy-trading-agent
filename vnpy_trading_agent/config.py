from __future__ import annotations

import os
import pathlib
from dataclasses import dataclass, replace
from typing import Any, Dict, Optional

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover - optional dependency at runtime
    yaml = None  # type: ignore


@dataclass(frozen=True)
class AppConfig:
    """Application configuration values.

    Extend this as your agent gains capabilities. Values are immutable to make
    configuration handling predictable and side-effect free.
    """

    log_level: str = "INFO"
    strategy_name: Optional[str] = None
    vt_symbol: Optional[str] = None
    config_path: Optional[str] = None


def _load_yaml_file(file_path: pathlib.Path) -> Dict[str, Any]:
    if yaml is None:
        raise RuntimeError(
            "PyYAML is required to load YAML config. Please install 'pyyaml'."
        )
    with file_path.open("r", encoding="utf-8") as file_handle:
        data = yaml.safe_load(file_handle) or {}
    if not isinstance(data, dict):
        raise ValueError("YAML root must be a mapping/object")
    return data


def load_config(path: Optional[str] = None) -> AppConfig:
    """Load configuration from YAML file and environment variables.

    Order of precedence (lowest to highest):
    - Defaults
    - YAML file values (if provided)
    - Environment variables
    """

    environment_path = os.environ.get("VNTA_CONFIG")
    config_path = path or environment_path

    config = AppConfig()

    if config_path:
        resolved_path = pathlib.Path(config_path).expanduser().resolve()
        if resolved_path.is_file():
            data = _load_yaml_file(resolved_path)
            config = AppConfig(
                log_level=str(data.get("log_level", config.log_level)).upper(),
                strategy_name=data.get("strategy_name", config.strategy_name),
                vt_symbol=data.get("vt_symbol", config.vt_symbol),
                config_path=str(resolved_path),
            )
        else:
            # Keep defaults but expose the attempted path for observability
            config = replace(config, config_path=str(resolved_path))

    # Environment variable overrides
    env_log = os.environ.get("VNTA_LOG_LEVEL")
    env_strategy = os.environ.get("VNTA_STRATEGY_NAME")
    env_vt_symbol = os.environ.get("VNTA_VT_SYMBOL")

    if env_log:
        config = replace(config, log_level=env_log.upper())
    if env_strategy:
        config = replace(config, strategy_name=env_strategy)
    if env_vt_symbol:
        config = replace(config, vt_symbol=env_vt_symbol)

    return config


def apply_overrides_from_cli(config: AppConfig, *, log_level: Optional[str] = None) -> AppConfig:
    """Apply command-line overrides to an AppConfig and return a new instance."""

    updated_config = config
    if log_level:
        updated_config = replace(updated_config, log_level=log_level.upper())
    return updated_config
