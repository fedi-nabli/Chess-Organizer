from modules.auth_module import AuthModule
from modules.user_info_module import UserInfoModule
from modules.drive_module import DriveModule
from modules.sheets_module import SheetsModule

from database.api import DataBaseApi

from utils.list_to_json import convert_list_to_dicts

def main():
  auth_session = AuthModule()
  user_info_instance = UserInfoModule(auth_session.creds)
  drive_instance = DriveModule(auth_session.creds)
  sheets_instance = SheetsModule(auth_session.creds)
  database_instance = DataBaseApi("ChessTestDB")
  files = drive_instance.list_files()
  user_info = user_info_instance.get_user_info()
  database_instance.create_users_table()
  database_instance.insert_user(user_info)
  # print(files)
  # print(sheets_instance.list_values(files[1].get('id')))
  # print(convert_list_to_dicts(sheets_instance.list_values(files[2].get('id'))))

if __name__ == '__main__':
  main()