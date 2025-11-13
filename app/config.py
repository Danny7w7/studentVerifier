import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqldb://root:@localhost/studentVerifier"
    SQLALCHEMY_TRACK_MODIFICATIONS = False