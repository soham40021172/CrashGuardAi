from pathlib import Path
import sys
from dotenv import load_dotenv
from loguru import logger

# --------------------------------------------------
# Load environment variables
# --------------------------------------------------
load_dotenv()

# --------------------------------------------------
# Project Paths
# --------------------------------------------------
PROJ_ROOT = Path(__file__).resolve().parents[1]

SRC_DIR = PROJ_ROOT / "crash_report"
PIPELINE_DIR = SRC_DIR / "pipeline"
CLEANING_DIR = PIPELINE_DIR / "cleaning"
FEATURE_DIR = PIPELINE_DIR / "feature_engineering"
MODELING_DIR = SRC_DIR / "modeling"
DB_DIR = SRC_DIR / "db"

DATA_DIR = PROJ_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

MODELS_DIR = PROJ_ROOT / "models"

REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

LOGS_DIR = PROJ_ROOT / "logs"

BACKEND_DIR = PROJ_ROOT / "backend"
BACKEND_MODELS_DIR = BACKEND_DIR / "models"
BACKEND_APP_DIR = BACKEND_DIR / "app"
BACKEND_LOGS = BACKEND_DIR / "logs"
APP_ROUTE = BACKEND_APP_DIR / "routes"
APP_SERVICES = BACKEND_APP_DIR / "services"
# Create required directories if they don't exist
for directory in [
    SRC_DIR, 
    PIPELINE_DIR, 
    CLEANING_DIR,
    FEATURE_DIR,
    MODELING_DIR, 
    DB_DIR,
    DATA_DIR,
    RAW_DATA_DIR,
    INTERIM_DATA_DIR,
    PROCESSED_DATA_DIR,
    EXTERNAL_DATA_DIR,
    MODELS_DIR,
    REPORTS_DIR,
    FIGURES_DIR,
    LOGS_DIR,
    BACKEND_DIR,
    BACKEND_MODELS_DIR,
    BACKEND_APP_DIR,
    BACKEND_LOGS,
    APP_ROUTE,
    APP_SERVICES
]:
    directory.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# Logging Configuration
# --------------------------------------------------

# Remove default logger
logger.remove()

# Console Logging (tqdm compatible if installed)
try:
    from tqdm import tqdm
    logger.add(lambda msg: tqdm.write(msg, end=""), colorize=True)
except ModuleNotFoundError:
    logger.add(sys.stdout, colorize=True)

# File Logging with rotation
logger.add(
    LOGS_DIR / "app_{time}.log",
    rotation="10 MB",          # rotate after 10MB
    retention="10 days",       # keep logs for 10 days
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} - {message}",
)

logger.success("Project configuration loaded successfully.")