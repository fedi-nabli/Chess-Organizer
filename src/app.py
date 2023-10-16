from flask import Flask
from modules.auth_module import AuthModule
from modules.drive_module import DriveModule

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

auth_session = AuthModule()
drive_instance = DriveModule(auth_session.creds)

@app.route('/')
def index():
  return 'API is running'

@app.route('/spreadsheets')
def list_spreadsheets():
  spreadhseets = drive_instance.list_files()
  return spreadhseets

if __name__ == '__main__':
  app.run(debug=True, port=15000)