import os
from environs import Env

env = Env()
env.read_env()

class FlaskrConfig:
  API_KEY = env("API_KEY")
  REDIS_URL = env("REDIS_URL")
  SECRET_KEY = env("SECRET_KEY")
  SQLALCHEMY_DATABASE_URI = env("SQLALCHEMY_DATABASE_URI")
