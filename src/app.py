from flask import Flask
from modules.auth_module import AuthModule
from modules.drive_module import DriveModule
from modules.sheets_module import SheetsModule

import database.api as db

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

db.init_database()
auth_session = AuthModule()
drive_instance = DriveModule(auth_session.creds)
sheets_instance = SheetsModule(auth_session.creds)

@app.route('/')
def index():
  return 'API is running'

@app.route('/spreadsheets')
def list_spreadsheets():
  spreadhseets = drive_instance.list_files()
  return spreadhseets

@app.route('/spreadsheets/<spreadsheet_id>')
def list_spreadsheet_values(spreadsheet_id=None):
  rows = sheets_instance.list_values(spreadsheet_id)
  return rows

if __name__ == '__main__':
  app.run(debug=True, port=15000)