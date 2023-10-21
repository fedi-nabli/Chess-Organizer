from modules.auth_module import AuthModule
from modules.drive_module import DriveModule
from modules.sheets_module import SheetsModule

def main():
  auth_session = AuthModule()
  drive_instance = DriveModule(auth_session.creds)
  sheets_instance = SheetsModule(auth_session.creds)
  files = drive_instance.list_files()
  print(files)
  print(sheets_instance.list_values(files[1].get('id')))

if __name__ == '__main__':
  main()