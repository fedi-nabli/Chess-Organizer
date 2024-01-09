from flask import Flask, request, jsonify
from modules.auth_module import AuthModule
from modules.drive_module import DriveModule
from modules.sheets_module import SheetsModule
from modules.user_info_module import UserInfoModule

from database.api import DataBaseApi

from utils.list_to_json import convert_list_to_dicts, convert_list_to_json

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

database_instance = DataBaseApi("ChessOrganizer")
auth_session = AuthModule()
user_info_instance = UserInfoModule(auth_session.creds)
drive_instance = DriveModule(auth_session.creds)
sheets_instance = SheetsModule(auth_session.creds)

# Initiate database tables
database_instance.create_users_table()
user_info = user_info_instance.get_user_info()
database_instance.insert_user(user_info)

@app.route('/')
def index():
  return 'API is running'

@app.route('/spreadsheets/list')
def list_spreadsheets():
  spreadhseets = drive_instance.list_files()
  return spreadhseets

@app.route('/spreadsheets')
def list_spreadsheets_json():
  spreadhseets = drive_instance.list_files()
  return convert_list_to_json(spreadhseets)

@app.route('/spreadsheets/<spreadsheet_id>/no-filter')
def list_spreadsheet_values_unfiltered(spreadsheet_id=None):
  rows = sheets_instance.list_values(spreadsheet_id)
  return rows

@app.route('/spreadsheets/<spreadsheet_id>/list')
def list_spreadsheet_values_list(spreadsheet_id=None):
  rows = sheets_instance.list_values(spreadsheet_id)
  return convert_list_to_dicts(rows)

@app.route('/spreadsheets/<spreadsheet_id>')
def list_spreadsheet_values(spreadsheet_id=None):
  rows = sheets_instance.list_values(spreadsheet_id)
  return convert_list_to_json(convert_list_to_dicts(rows))

@app.route('/users')
def list_users():
  users = database_instance.get_users()
  return convert_list_to_json(users)

@app.route('/users/search/<name>')
def search_user_by_name(name: str = None):
  users = database_instance.search_for_user(name)

@app.route('/users/<email>')
def search_user_by_email(email: str = None):
  users = database_instance.search_for_user(email=email)
  return convert_list_to_json(users)

@app.route('/users/update/<id>', methods=['POST'])
def update_user_name(id: int = None):
  data = request.get_json()
  name = data['name']
  users = database_instance.update_user_name(id, name)
  return convert_list_to_json(users)

@app.route('/users/<id>', methods=['DELETE'])
def delete_user_by_id(id: int = None):
  database_instance.delete_user_by_id(id)
  return jsonify(True)

if __name__ == '__main__':
  app.run(debug=True, port=15000)