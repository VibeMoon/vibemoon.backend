from pathlib import Path
import dj_database_url

from .env_reader import env, csv

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = env("SECRET_KEY")
DATABASE_URL = env("DATABASE_URL")
ALLOWED_HOSTS = env("ALLOWED_HOSTS", cast=csv())


DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL)
}