"""
shared logger used by every other steps 
Every module can import this logger and use it to log messages consistently across the application.
"""

import logging
import os
from datetime import datetime

# Current date
_run_started_at = datetime.now()
_run_date = _run_started_at.strftime("%Y-%m-%d")
_run_time = _run_started_at.strftime("%H-%M-%S")

# Create date-wise log directory
LOGS_DIR = os.path.join("logs", _run_date)
os.makedirs(LOGS_DIR, exist_ok=True)

# Create a log file for this particular run
RUN_LOG_FILE = os.path.join(
    LOGS_DIR,
    f"hr_assistant_{_run_time}.log"
)

_logger = logging.getLogger("hr_assistant")
_logger.setLevel(logging.INFO)
_logger.propagate = False

if not _logger.handlers:
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )
    file_handler = logging.FileHandler(RUN_LOG_FILE, encoding="utf-8")
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    _logger.addHandler(file_handler)
    _logger.addHandler(stream_handler)

logger = _logger

def get_logger(name: str) -> logging.Logger:
    """Get a logger instance with the specified name."""
    return _logger.getChild(name)