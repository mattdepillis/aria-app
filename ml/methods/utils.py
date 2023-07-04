# import packages
from dotenv import load_dotenv
import os


load_dotenv()
SPOTIFY_API_CLIENT_ID = os.getenv('SPOTIFY_API_CLIENT_ID')

def conditional(x, y):
    return x > y




if __name__ == "__main__":
    print(SPOTIFY_API_CLIENT_ID)

