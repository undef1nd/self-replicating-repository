import os

from flask import Flask, redirect, request, session, url_for
from requests_oauthlib import OAuth2Session

# This information is obtained upon registration of the new GitHub OAuth
# application here: https://github.com/settings/applications/new
# URLs taken from here: https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
APP_SECRET = os.getenv('APP_SECRET', 'development')
REPO_OWNER = os.getenv('REPO_OWNER', 'undef1nd')
REPO_NAME = os.getenv('REPO_NAME', 'self-replicating-repository')

API_BASE_URL = 'https://api.github.com'
AUTH_BASE_URL = 'https://github.com/login/oauth/authorize'
TOKEN_URL = 'https://github.com/login/oauth/access_token'

# Setting up Flask
app = Flask(__name__)
app.secret_key = APP_SECRET


@app.route('/')
def auth():
    """Redirect the user to GitHub OAuth url - AUTH_BASE_URL
    Set the scope read/write public repos as per
    https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/
    """
    github = OAuth2Session(CLIENT_ID, scope='public_repo')
    authorization_url, state = github.authorization_url(AUTH_BASE_URL)
    return redirect(authorization_url)


@app.route('/callback/github')
def callback():
    """Get user's token after redirect from GitHub"""
    github = OAuth2Session(CLIENT_ID)
    token = github.fetch_token(TOKEN_URL, client_secret=CLIENT_SECRET, authorization_response=request.url)
    session['auth_token'] = token
    return redirect(url_for('repl'))


@app.route('/repl')
def repl():
    """Forking the repository specified in REPO_OWNER/REPO_NAME"""
    if not session['auth_token']:
        return 'Something wrong here... Your authorization failed.'

    github = OAuth2Session(CLIENT_ID, token=session['auth_token'])
    response = github.post(f'{API_BASE_URL}/repos/{REPO_OWNER}/{REPO_NAME}/forks')

    if response.status_code == 404:
        return 'Ahhh! The requested repository does not exist.'

    if not response.ok:
        return 'Something wrong here...Don\'t hesitate to contact the owner of the code.'

    return f'Congrats! You\'ve successfully forked the repository: \n ' \
        f'<a href="https://github.com/{response.json()["full_name"]}">{REPO_NAME}</a>.'


if __name__ == "__main__":
    # Uncomment the below line to run via HTTP - don't use in production
    # os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    app.run()
