from __future__ import print_function
import os.path

# Google auth imports
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

class AuthModule():
  def __init__(self) -> None:
    self.SCOPES = ['openid', 'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile', 'https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.metadata.readonly']
    self.creds = None
    
    if os.path.exists('token.json'):
      self.creds = Credentials.from_authorized_user_file('token.json', scopes=self.SCOPES)
    if not self.creds or not self.creds.valid:
      if self.creds and self.creds.expired and self.creds.refresh_token:
        try:
          self.creds.refresh(Request())
        except:
          os.remove('token.json')
          flow = InstalledAppFlow.from_client_secrets_file('credentials.json', scopes=self.SCOPES)
          self.creds = flow.run_local_server(port=0)
      else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', scopes=self.SCOPES)
        self.creds = flow.run_local_server(port=0)
      with open('token.json', 'w') as token:
        token.write(self.creds.to_json())