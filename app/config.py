import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqldb://{os.getenv("db_user")}:{os.getenv("db_pass")}@localhost/{os.getenv("db_name")}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False