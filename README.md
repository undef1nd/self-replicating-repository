# Self-Replicating Repository

This repository contains the Python code that forks itself into User's GitHub profile.

## Flow Overview

1. User clicks on the link of the deployed application. For example, [some_link_to_heroku]()
2. User is redirected to GitHub site to allow access to his/her public profile for the application.
3. Application forks its own repository into User's GitHub profile.

## Installation
The code can be run locally or deployed to any hosting of your choise. For example, to Heroku. 

## Installation Prerequisites
No matter what type of installation is chosen you need to register your application via GitHub.
1. Go to [Register a new OAuth application.
](https://github.com/settings/applications/new)
2. Give your app some meaningful **Application name**. **Application desscription** is optional.
3. In **Homepage URL** specify the one for your application:
[http://127.0.0.1:5000](http://127.0.0.1:5000) if you deploy locally or [some_link_to_heroku]() for Heroku
4. In **Authorization Callback URL** specify [http://127.0.0.1:5000/callback/github](http://127.0.0.1:5000/callback/github) for localhost or [some_link_to_heroku/callback/github](/callback/github) for Heroku
5. Save **client_id** and **client_secret** as they'll be needed in the next steps.


## Local Installation

1. Clone the repository:
```bash
git clone https://github.com/undef1nd/self-replicating-repository.git && cd self-replicating-repository
```

2. Create a separate Python environment for application and install required modules:

```bash
pip3 install virtualenv
virtualenv app_env
source app_env/bin/activate
pip install -r requirements.txt
```

3. Set environment variables to your own values:

```bash
export CLIENT_ID=your_github_client_id
export CLIENT_SECRET=your_github_client_secret
export APP_SECRET=your_app_secret_id
export REPO_OWNER=github_repository_owner
export REPO_NAME= github_repository_that_will_be_forked
```
For **CLIENT_ID** and **CLIENT_SECRET** values paste those obtained while registering app at GitHub (see *Installation Prerequisites* section).

**APP_SECRET** is the secret key for Flask app that should not be exposed. You can use the output of the below snippet to generate key or come up with your own phrase:
```python
import os
os.urandom(24)
```
4. **This should not be done in prod!**
Normally OAuth2 is not used over HTTP, but it can be useful for local testing. In order to achieve that set either set environment variable:
```bash
export OAUTHLIB_INSECURE_TRANSPORT=1
```
or uncomment the following line in *repl_app.py* file:
```python
 os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"
```
5. Finally run the application:
```bash
python repl_app.py
```
6. Go to [http://127.0.0.1:5000](http://127.0.0.1:5000). If everything is done correctly you get your the repository forked to your profile. Congrats!

## Heroku Installation
1. Login to Heroku and go [create new app](https://dashboard.heroku.com/new-app)
2. Give name to your app in **App name** field. 
3. On the next page choose **GitHub** as the **Deployment method**. 
