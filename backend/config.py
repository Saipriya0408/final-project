"""
SymptoCare Backend Configuration
Loads settings from environment variables with sensible defaults.
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Base configuration loaded from environment variables."""

    # Server
    PORT: int = int(os.getenv("PORT", 5000))
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    HOST: str = os.getenv("HOST", "0.0.0.0")

    # Paths (resolved relative to backend/ root)
    BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR: str = os.path.join(BASE_DIR, os.getenv("DATA_DIR", "data"))
    DOCTORS_DB_PATH: str = os.path.join(
        BASE_DIR, os.getenv("DOCTORS_DB_PATH", "database/doctors.json")
    )
    HOSPITALS_DB_PATH: str = os.path.join(
        BASE_DIR, os.getenv("HOSPITALS_DB_PATH", "database/hospitals.json")
    )

    # Data file names (relative to DATA_DIR)
    SYMPTOM_CSV: str = "Symptom.csv"
    SEVERITY_CSV: str = "Symptom Severity.csv"
    DESCRIPTION_CSV: str = "Symptom Description.csv"
    PRECAUTION_CSV: str = "Symptom Precaution.csv"
    SPECIALIST_CSV: str = "Disease Specialist.csv"

    # ML settings
    MAX_SYMPTOMS: int = int(os.getenv("MAX_SYMPTOMS", 5))
    MIN_SYMPTOMS: int = int(os.getenv("MIN_SYMPTOMS", 1))
    RF_N_ESTIMATORS: int = 100
    RF_RANDOM_STATE: int = 9        # Same split used in original repo
    RF_TEST_SIZE: float = 0.25      # Same as original repo

    # Doctor/hospital search
    DEFAULT_SEARCH_RADIUS_KM: float = float(
        os.getenv("DEFAULT_SEARCH_RADIUS_KM", 25)
    )
    MAX_RESULTS_DOCTORS: int = int(os.getenv("MAX_RESULTS_DOCTORS", 50))
    MAX_RESULTS_HOSPITALS: int = int(os.getenv("MAX_RESULTS_HOSPITALS", 50))
    DEFAULT_CITY: str = os.getenv("DEFAULT_CITY", "Chennai")

    # CORS
    ALLOWED_ORIGINS: list = os.getenv("ALLOWED_ORIGINS", "*").split(",")


config = Config()
