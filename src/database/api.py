import os
from os.path import join, dirname
from dotenv import load_dotenv
import mysql.connector as connector

dotnev_path = join(dirname(__file__), '../../.env')
load_dotenv(dotnev_path)

DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_USERNAME = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASS')

def init_database(db_name: str = None):
  connection = connector.connect(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USERNAME,
    password=DB_PASSWORD
  )
  print('Connection established successfully')
  cursor = connection.cursor()
  if db_name is not None:
    create_db_query = f"""CREATE DATABASE IF NOT EXISTS {db_name}"""
    cursor.execute(create_db_query)
    use_db_query = f"""USE {db_name}"""
    cursor.execute(use_db_query)