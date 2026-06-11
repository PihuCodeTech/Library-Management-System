import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# Database
DB_CONFIG = {
    "host":             os.getenv("DB_HOST", "localhost"),
    "user":             os.getenv("DB_USER", "root"),
    "password":         os.getenv("DB_PASSWORD", ""),
    "database":         os.getenv("DB_NAME", "library_management_system"),
    "charset":          "utf8mb4",
    "autocommit":       False,
    "connect_timeout":  10,
}

DB_POOL_NAME = "library_pool"
DB_POOL_SIZE = int(os.getenv("DB_POOL_SIZE", "5"))

# Business rules
LOAN_DURATION_DAYS    = int(os.getenv("LOAN_DURATION_DAYS", "14"))
FINE_PER_DAY_RS       = int(os.getenv("FINE_PER_DAY_RS", "10"))
MAX_BOOKS_PER_STUDENT = int(os.getenv("MAX_BOOKS_PER_STUDENT", "3"))

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_FILE  = os.getenv("LOG_FILE", str(BASE_DIR / "logs" / "library.log"))

# Display
PAGE_SIZE = int(os.getenv("PAGE_SIZE", "20"))