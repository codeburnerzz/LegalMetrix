import os
from typing import List


class Settings:
    PROJECT_NAME: str = "LEGAL METRIX Enforcement Backend"
    API_V1_STR: str = "/api/v1"

    # Secret key for JWT encoding/decoding
    SECRET_KEY: str = os.getenv(
        "SECRET_KEY",
        "legalmetrix-sih2026-super-secure-enforcement-key-9941"
    )
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours

    # CORS Origins
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",

        # Render frontend
        "https://legalmetrix-cp08.onrender.com",

        # Add your Vercel frontend URL here after deployment
        # Example:
        # "https://your-frontend.vercel.app",
    ]

    # SQLite database
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "sqlite:///./legalmetrix.db"
    )

    # Vercel provides a read-only deployment filesystem.
    # /tmp is writable during the serverless execution.
    UPLOAD_DIR: str = os.path.join(
        "/tmp",
        "legalmetrix_uploads"
    )


settings = Settings()

# Create writable temporary upload directory
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)