from __future__ import print_function
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class UserInfoModule():
  def __init__(self, creds: Credentials = None) -> None:
    try:
      self.services = build('oauth2', 'v2', credentials=creds)

    except HttpError as error:
      print(f'An error occured: {error}')

  def get_user_info(self) -> dict:
    try:
      user_info = self.services.userinfo().get().execute()
      return user_info

    except HttpError as error:
      print(f'An error occured: {error}')