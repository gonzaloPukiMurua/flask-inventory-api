import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:tu_password@localhost:5432/stock_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False