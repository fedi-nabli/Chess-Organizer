from modules.auth_module import AuthModule
from modules.drive_module import DriveModule
from modules.sheets_module import SheetsModule

from database.api import init_database

from utils.list_to_json import convert_list_to_dicts

def main():
  auth_session = AuthModule()
  drive_instance = DriveModule(auth_session.creds)
  sheets_instance = SheetsModule(auth_session.creds)
  init_database()
  files = drive_instance.list_files()
  # print(files)
  # print(sheets_instance.list_values(files[1].get('id')))
  print(convert_list_to_dicts(sheets_instance.list_values(files[2].get('id'))))

if __name__ == '__main__':
  main()