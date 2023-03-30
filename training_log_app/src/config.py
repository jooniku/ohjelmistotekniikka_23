import os, sys
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, '..', '.env'))
except FileNotFoundError:
    pass

DATABASE_FILENAME = os.getenv('DATABASE_FILENAME') or 'default database.sqlite'
DATABASE_FILEPATH = os.getenv('DATABASE_FILEPATH') or os.path.join(dirname, '..', 'data', DATABASE_FILENAME)
