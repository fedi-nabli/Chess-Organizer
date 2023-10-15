from modules.auth_module import AuthModule
from modules.drive_module import DriveModule

def main():
  auth_session = AuthModule()
  drive_instance = DriveModule(auth_session.creds)
  print(drive_instance.list_files())

if __name__ == '__main__':
  main()