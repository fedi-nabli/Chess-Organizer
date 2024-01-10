import streamlit as st

from modules.auth_module import AuthModule
from modules.drive_module import DriveModule
from modules.sheets_module import SheetsModule
from modules.user_info_module import UserInfoModule

from database.api import DataBaseApi

database_instance = DataBaseApi("ChessOrganizerWeb")
auth_session = AuthModule()
user_info_instance = UserInfoModule(auth_session.creds)
drive_instance = DriveModule(auth_session.creds)
sheets_instance = SheetsModule(auth_session.creds)

# Initiate database tables
database_instance.create_users_table()
user_info = user_info_instance.get_user_info()
database_instance.insert_user(user_info)

st.title("Chess Organizer")
st.markdown("This little app allows you to connect to your google account and extract users and sheet data")

def get_sheet_id_from_name(name: str = None, spreadsheets: list = None):
  for sheet in spreadsheets:
    if sheet.get('name') == name:
      return sheet.get('id')

def home():
  st.write("Choose a file from the dropdown")
  files = drive_instance.list_files()
  spredsheets = [file.get('name') for file in files]
  selected_sheet = st.selectbox("Select a sheet", spredsheets)
  sheet_id = get_sheet_id_from_name(selected_sheet, files)
  rows = sheets_instance.list_values(sheet_id)
  st.table(rows)
  database_instance.create_spreadsheet_table(rows)

def search_users():
  users = database_instance.get_users()
  st.table(users)
  col1, col2 = st.columns(2)
  with col1:
    username = st.text_input("Enter user name to search:", "Enter user name to search:")
    if username != "":
      users = database_instance.search_for_user(username)
      st.write("Filtered Users")
      st.table(users)
  with col2:
    email = st.text_input("Enter user email to search:", "Enter user email to search:")
    if email != "":
      users = database_instance.search_for_user(email=email)
      st.write("Filtered Users")
      st.table(users)

def users():
  users = database_instance.get_users()
  st.table(users)
  selected_row = st.table(user_info).selectbox('Select a row', options=list(range(len(users))))

  if selected_row is not None:
    selected_user = users[selected_row]
    user_name = st.text_input("Enter new user name", selected_user.get('Name'))
    col1, col2 = st.columns(2)
    with col1:
      if st.button("Update name of selected user"):
        database_instance.update_user_name(selected_user.get('ID'), user_name)
        st.rerun()
    with col2:
      if st.button("Delete selected user"):
        database_instance.delete_user_by_id(selected_user.get('ID'))
        st.rerun()

st.sidebar.markdown("Choose a file, see a sheet or see users")
_radio = st.sidebar.radio("Navigation", ("Choose file", "Search and Filter Users", "Update Users Data"))

if _radio == "Choose file":
  home()
elif _radio == "Search and Filter Users":
  search_users()
elif _radio == "Update Users Data":
  users()