import os
from dotenv import load_dotenv

load_dotenv()

class Config:
   SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_PROD')
   SECRET_KEY = 'bedigital'
   JWT_SECRET_KEY = 'bedigital'