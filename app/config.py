from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    DATABASE_HOST: str = os.getenv("DATABASE_HOST") or ""
    DATABASE_NAME: str = os.getenv("DATABASE_NAME") or ""
    DATABASE_USER: str = os.getenv("DATABASE_USER") or ""
    DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD") or ""
