from pathlib import Path

from loguru import logger


LOG_DIR = Path('logs')
LOG_DIR.mkdir(exist_ok=True)

logger.add(
    LOG_DIR / 'climate_engine.log',
    rotation='5 MB',
    retention=5,
    level='INFO',
)


def get_logger():
    return logger
