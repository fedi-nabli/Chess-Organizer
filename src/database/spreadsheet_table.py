from mysql.connector import MySQLConnection, Error
from mysql.connector.cursor import MySQLCursor

from utils.list_to_tuple import convert_list_to_tuple

def create_table_from_dict(connection: MySQLConnection = None, cursor: MySQLCursor = None, data_rows: list[tuple] = None, column_types: dict = None, table_name: str = 'dynamic_table'):
    # Constructing CREATE TABLE query using dictionary keys and values
    columns = ', '.join([f'{key} {value}' for key, value in column_types.items()])
    create_table_query = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns})'

    # Execute CREATE TABLE query
    cursor.execute(create_table_query)

    # Inserting data from list into the table
    for row in data_rows:
      insert_query = "INSERT INTO spreadsheets VALUES (%s, %s, %s, %s, %s, %s)"
      values = (row[0], row[1], row[2], row[3], row[4], row[5])
      cursor.execute(insert_query, values)

    # Commit changes and close connection
    connection.commit()

def create_spreadsheets_table(connection: MySQLConnection = None, cursor: MySQLCursor = None, rows: list[list] = None) -> bool:
  try:
    column_types = {
      'Name': 'TEXT',
      'NumTel': 'CHAR(8)',
      'DOB': 'VARCHAR(20)',
      'FIDE_ID': 'INTEGER',
      'Ville': 'TEXT',
      'ELO': 'INT'
    }

    create_table_from_dict(connection, cursor, convert_list_to_tuple(rows), column_types, 'spreadsheets')
    return True

  except Error as err:
    print(f'An error occured: {err}')
    return False

def list_spreadsheet_data(cursor: MySQLCursor = None) -> list[dict]:
  spreadsheet_datat = []
  try:
    select_spreadsheet_data_query = """SELECT * FROM spreadsheetS"""
    cursor.execute(select_spreadsheet_data_query)
    spreadsheets = cursor.fetchall()
    for spreadsheet_row in spreadsheets:
      spreadsheet: dict = {}
      spreadsheet['Name'] = spreadsheet_row[0]
      spreadsheet['NumTel'] = spreadsheet_row[1]
      spreadsheet['DOB'] = spreadsheet_row[2]
      spreadsheet['FIDE ID'] = spreadsheet_row[3]
      spreadsheet['Club/Ville'] = spreadsheet_row[4]
      spreadsheet['ELO'] = spreadsheet_row[5]
      spreadsheet_datat.append(spreadsheet)
    return spreadsheet_datat

  except Error as err:
    print(f'An error occured: {err}')
    return spreadsheet_datat