from mysql.connector import MySQLConnection, Error
from mysql.connector.cursor import MySQLCursor

def create_users_table(cursor: MySQLCursor = None):
  try:
    create_users_table_query = """
                                CREATE TABLE IF NOT EXISTS USERS (
                                  ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                                  Name VARCHAR(150) NOT NULL,
                                  Email VARCHAR(250)
                                )
                              """
    cursor.execute(create_users_table_query)

  except Error as err:
    print(f'An error occured: {err}')

def insert_users_into_table(connection: MySQLConnection = None, cursor: MySQLCursor = None, user: dict = None) -> bool:
  try:
    select_users_query = """SELECT * FROM USERS"""
    cursor.execute(select_users_query)
    res = cursor.fetchall()
    for user_res in res:
      if user_res[2] == user['email']:
        return True
    insert_users_query = """INSERT INTO USERS (Name, Email) VALUES (%s, %s)"""
    values = (user['name'], user['email'])
    cursor.execute(insert_users_query, values)
    connection.commit()
    return True
  
  except Error as err:
    print(f'An error occured while inserting: {err}')
    return False
  
def list_users(cursor: MySQLCursor = None) -> list[dict]:
  users_list = []
  try:
    select_users_query = """SELECT * FROM USERS"""
    cursor.execute(select_users_query)
    users = cursor.fetchall()
    for user_res in users:
      user: dict = {}
      user['ID'] = user_res[0]
      user['Name'] = user_res[1]
      user['Email'] = user_res[2]
      users_list.append(user)
      return users_list

  except Error as err:
    print(f'An error occured: {err}')
    return users_list