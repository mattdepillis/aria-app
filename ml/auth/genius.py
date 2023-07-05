# imports
import base64
from dotenv import load_dotenv
import os
import requests
import urllib

# read environment variables
load_dotenv()
# client id and secret
GENIUS_API_CLIENT_ID = os.getenv('GENIUS_API_CLIENT_ID')
GENIUS_API_CLIENT_SECRET = os.getenv('GENIUS_API_CLIENT_SECRET')
# access token
GENIUS_API_ACCESS_TOKEN = os.getenv('GENIUS_API_ACCESS_TOKEN')
# redirect uri
GENIUS_API_REDIRECT_URI = os.getenv('GENIUS_API_REDIRECT_URI')

def get_access_token():
  return