import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

class Config:
    # Database URL
    DB_URL = (
        f"postgresql+psycopg2://{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}:"
        f"{os.getenv('DB_PORT')}/"
        f"{os.getenv('DB_NAME')}"
    )

    # Flask general secret key
    SECRET_KEY = os.getenv("SECRET_KEY", "my_flask_secret_key")

    # JWT secret key
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "my_jwt_secret_key")

    # Optional: JWT settings
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)

print("Connecting to database:", Config.DB_URL)