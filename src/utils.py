"""
Common utility functions used across the project.
"""

from pathlib import Path
import logging


def create_directory(directory_path: Path) -> None:
    """
    Create a directory if it does not exist.

    Parameters
    ----------
    directory_path : Path
        Directory path to create.
    """
    directory_path.mkdir(parents=True, exist_ok=True)


def configure_logger(log_file: Path) -> logging.Logger:
    """
    Configure project logger.

    Parameters
    ----------
    log_file : Path
        Path of log file.

    Returns
    -------
    logging.Logger
        Configured logger instance.
    """
    logger = logging.getLogger("patient_readmission")

    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(log_file)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger