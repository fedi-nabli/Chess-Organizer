from __future__ import print_function
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class SheetsModule():
  def __init__(self, creds: Credentials = None) -> None:
    try:
      self.services = build('sheets', 'v4', credentials=creds)

    except HttpError as error:
      print(f'An error occured: {error}')
  
  def list_values(self, spreadsheet_id: str = None) -> list:
    try:
      rows = []

      spreadhseet = self.services.spreadsheets().get(
        spreadsheetId=spreadsheet_id
      ).execute()
      range = spreadhseet['sheets'][0]['properties']['title']

      result = self.services.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range
      ).execute()

      rows.extend(result.get('values', []))
      
    except HttpError as error:
      print(f'An error occured: {error}')

    return rows