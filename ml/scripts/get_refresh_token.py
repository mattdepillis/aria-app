"""
This script should be used in the event that the application requires a new refresh token to be generated.
"""

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
# api url
SPOTIFY_API_AUTH_URL = os.getenv('SPOTIFY_API_AUTH_URL')
# redirect uri
SPOTIFY_API_REDIRECT_URI = os.getenv('SPOTIFY_API_REDIRECT_URI')

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


if __name__ == "__main__":
    url = get_refresh_token_access_code_url()
    print(url)
    """
    Visit URL and approve. Then, set AUTH_CODE to the code in the resulting url from the page redirect after approval.
    """
    AUTH_CODE = '<CODE>'

    # * once AUTH_CODE is obtained, uncomment and run the following
    # token = get_refresh_token(AUTH_CODE)
    # print(token)