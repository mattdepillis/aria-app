# imports
import base64
from dotenv import load_dotenv
import os
import requests
import urllib

# read environment variables
load_dotenv()
# client id and secret
SPOTIFY_API_CLIENT_ID = os.getenv('SPOTIFY_API_CLIENT_ID')
SPOTIFY_API_CLIENT_SECRET = os.getenv('SPOTIFY_API_CLIENT_SECRET')
# refresh token
SPOTIFY_REFRESH_TOKEN = os.getenv('SPOTIFY_REFRESH_TOKEN')
# urls
SPOTIFY_API_AUTH_URL = os.getenv('SPOTIFY_API_AUTH_URL')
SPOTIFY_API_TOKEN_URL= os.getenv('SPOTIFY_API_TOKEN_URL')
# redirect uri
SPOTIFY_API_REDIRECT_URI = os.getenv('SPOTIFY_API_REDIRECT_URI')


def get_access_token():
    # Construct the request URL with query parameters
    url = f"{SPOTIFY_API_TOKEN_URL}?grant_type=refresh_token&refresh_token={SPOTIFY_REFRESH_TOKEN}"

    # Encode the client ID and client secret in base64
    client_credentials = f"{SPOTIFY_API_CLIENT_ID}:{SPOTIFY_API_CLIENT_SECRET}"
    base64_credentials = base64.b64encode(client_credentials.encode()).decode()

    # Send a POST request to the token endpoint
    response = requests.post(url, headers={
        "Authorization": f"Basic {base64_credentials}",
        "Content-Type": "application/x-www-form-urlencoded"
    })

    # Parse the JSON response and extract the access token
    data = response.json()
    access_token = data.get("access_token")

    return access_token

"""
This script should be used in the event that the application requires a new refresh token to be generated.
"""

def get_refresh_token_access_code_url():
    params = {
        'client_id': SPOTIFY_API_CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': SPOTIFY_API_REDIRECT_URI,
        'scope': 'ugc-image-upload user-read-playback-state user-modify-playback-state user-read-currently-playing app-remote-control streaming playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public user-follow-modify user-follow-read user-read-playback-position user-top-read user-read-recently-played user-library-modify user-library-read user-read-email user-read-private'
    }
    auth_url = f'{SPOTIFY_API_AUTH_URL}?{urllib.parse.urlencode(params)}'
    return auth_url
    
def get_refresh_token(auth_code):
    # Set up the required parameters
    client_id = SPOTIFY_API_CLIENT_ID
    client_secret = SPOTIFY_API_CLIENT_SECRET
    redirect_uri = SPOTIFY_API_REDIRECT_URI
    authorization_code = auth_code

    # Encode the client ID and client secret
    credentials = base64.b64encode(f'{client_id}:{client_secret}'.encode('utf-8')).decode('utf-8')

    # Prepare the token endpoint URL
    token_url = 'https://accounts.spotify.com/api/token'

    # Make a POST request to the token endpoint
    response = requests.post(token_url, data={
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'redirect_uri': redirect_uri
    }, headers={
        'Authorization': f'Basic {credentials}'
    })

    # Parse the response JSON
    data = response.json()
    print(data)

    # Extract the refresh token from the response
    refresh_token = data.get('refresh_token')

    return refresh_token