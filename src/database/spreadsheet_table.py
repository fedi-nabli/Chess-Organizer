from mysql.connector import MySQLConnection, Error
from mysql.connector.cursor import MySQLCursor

from utils.list_to_tuple import convert_list_to_tuple

def create_table_from_dict(connection: MySQLConnection = None, cursor: MySQLCursor = None, data_rows: list[tuple] = None, column_types: list = None, table_name: str = 'dynamic_table'):
    # Constructing CREATE TABLE query using dictionary keys and values
    columns = ', '.join([f'{key} {value}' for key, value in data_rows.items()])
    create_table_query = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns})'

    # Execute CREATE TABLE query
    cursor.execute(create_table_query)

    # Inserting data from list into the table
    insert_query = f'INSERT INTO {table_name} VALUES ({", ".join(["%s" for _ in range(len(data_rows))])})'
    cursor.executemany(insert_query, column_types)

    # Commit changes and close connection
    connection.commit()

def create_spreadsheets_table(connection: MySQLConnection = None, cursor: MySQLCursor = None, rows: list[list] = None) -> bool:
  try:
    column_types = {
      'FIDE ID': 'INTEGER',
      'Name': 'TEXT',
      'NumTel': 'CHAR(8)',
      'DOB': 'DATE',
      'Club/Ville': 'VARCHAR(30)',
      'ELO': 'INT'
    }

    create_table_from_dict(connection, cursor, convert_list_to_tuple(rows), column_types, 'spreadsheets.')
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
      spreadsheet['FIDE ID'] = spreadsheet_row[0]
      spreadsheet['Name'] = spreadsheet_row[1]
      spreadsheet['NumTel'] = spreadsheet_row[2]
      spreadsheet['DOB'] = spreadsheet_row[3]
      spreadsheet['Club/Ville'] = spreadsheet_row[4]
      spreadsheet['ELO'] = spreadsheet_row[5]
      spreadsheet_datat.append(spreadsheet)
    return spreadsheet_datat

  except Error as err:
    print(f'An error occured: {err}')
    return spreadsheet_datat