import spotify

if __name__ == "__main__":
    url = spotify.get_refresh_token_access_code_url()
    print(url)
    """
    Visit URL and approve. Then, set AUTH_CODE to the code in the resulting url from the page redirect after approval.
    """
    AUTH_CODE = '<CODE>'

    # * once AUTH_CODE is obtained, uncomment and run the following
    # token = spotify.get_refresh_token(AUTH_CODE)
    # print(token)