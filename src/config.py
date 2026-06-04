"""
Project-wide configuration settings.
"""

from pathlib import Path

PROJECT_ROOT: Path = Path(__file__).resolve().parent.parent

DATA_DIR: Path = PROJECT_ROOT / "data"
MODELS_DIR: Path = PROJECT_ROOT / "models"
REPORTS_DIR: Path = PROJECT_ROOT / "reports"
LOGS_DIR: Path = PROJECT_ROOT / "logs"

DATABASE_PATH: Path = DATA_DIR / "patient_readmission.db"

RANDOM_STATE: int = 42

TARGET_COLUMN: str = "readmitted"