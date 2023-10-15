from __future__ import print_function
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class DriveModule():
  def __init__(self, creds: Credentials = None) -> None:
    try:
      self.services = build('drive', 'v3', credentials=creds)
    
    except HttpError as error:
      print(f'An error occured: {error}')

  def list_files(self) -> list:
    try:
      files = []
      page_token = None
      while True:
        response = self.services.files().list(
          q="mimeType='application/vnd.google-apps.spreadsheet'",
          spaces='drive',
          fields='nextPageToken, '
                  'files(id, name)',
          pageToken=page_token
        ).execute()

        files.extend(response.get('files', []))
        page_token = response.get('nextPageToken', None)
        if page_token is None:
          break

    except HttpError as error:
      print(f'An error occured: {error}')

    return files