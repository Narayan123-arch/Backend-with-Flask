import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_URL=f"postgresql+psycopg2://{os.getenv('DB_USER')}:"\
    f"{os.getenv('DB_PASSWORD')}@"\
    f"{os.getenv('DB_HOST')}:" \
    f"{os.getenv('DB_PORT')}/" \
    f"{os.getenv('DB_NAME')}"
print("connecting to database",Config.DB_URL)