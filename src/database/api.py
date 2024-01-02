import os
import re
from os.path import join, dirname
from dotenv import load_dotenv
import mysql.connector as connector

from database.user_table import create_users_table, insert_users_into_table, list_users,find_user_by_name, find_user_by_email

dotnev_path = join(dirname(__file__), '../../.env')
load_dotenv(dotnev_path)

DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_USERNAME = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASS')

class DataBaseApi():
  def __init__(self, db_name: str = None, delete_if_exists: bool = False) -> None:
    self.connection = connector.connect(
      host=DB_HOST,
      port=DB_PORT,
      user=DB_USERNAME,
      password=DB_PASSWORD
    )
    print('Connection established successfully')
    self.cursor = self.connection.cursor()

    self.cursor.execute("SHOW DATABASES")
    self.found = False
    for db in self.cursor:
      pattern = "[(,')]"
      db_string = re.sub(pattern, "", str(db))
      if db_string == db_name.lower():
        self.found = True
        print(f'Database {db_name} exists')

    if db_name is not None:
      if self.found == False and not delete_if_exists:
        create_db_query = f"""CREATE DATABASE {db_name}"""
        self.cursor.execute(create_db_query)
        print(f'Created {db_name} db')
      elif self.found:
        if delete_if_exists:
          drop_db_query = f"""DROP DATABASE {db_name}"""
          self.cursor.execute(drop_db_query)
          create_db_query = f"""CREATE DATABASE {db_name}"""
          self.cursor.execute(create_db_query)
          print(f'Created {db_name} db')
        use_db_query = f"""USE {db_name}"""
        self.cursor.execute(use_db_query)

  def create_users_table(self) -> bool:
    return create_users_table(self.cursor)

  def insert_user(self, user: dict) -> bool:
    return insert_users_into_table(self.connection, self.cursor, user)
  
  def get_users(self) -> list[dict]:
    return list_users(self.cursor)
  
  def search_for_user(self, username: str = None, email: str = None) -> list[dict]:
    users = []
    if email is not None:
      return find_user_by_email(self.cursor, email)
    elif username is not None:
      return find_user_by_name(self.cursor, username)
    else:
      return users