# Self-Replicating Repository

This repository contains the Python code that forks itself into User's GitHub profile.

## Flow Overview

1. User clicks on the link of the deployed application. For example, [https://self-repl-repo.herokuapp.com/](https://self-repl-repo.herokuapp.com/)
2. User is redirected to GitHub site to allow access to his/her public profile for the application.
3. Application forks its own repository into User's GitHub profile.

## Installation
The code can be run either locally or deployed anywhere else. Instructions for deployment to Heroku can be found below.

### Installation Prerequisites
No matter what type of installation is chosen you need to register your new application at GitHub.
1. Go to [Register a new OAuth application.
](https://github.com/settings/applications/new)
2. Give your app some meaningful **Application name**. **Application description** is optional.
3. In **Homepage URL** specify the one for your application:
[http://127.0.0.1:5000]() if you deploy locally or [https://[*your_app_name*].herokuapp.com/]() for Heroku. 
4. In **Authorization Callback URL** specify [http://127.0.0.1:5000/callback/github]() for localhost or [https://[*your_app_name*].herokuapp.com/callback/github]() for Heroku.
5. Save **Client ID** and **Client Secret** as they are needed in the next steps.

You can change Homepage and Authorization Callback URLs any time.


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

3. Set environment variables with your own values:

```bash
export CLIENT_ID=your_github_client_id
export CLIENT_SECRET=your_github_client_secret
export APP_SECRET=your_app_secret_id
```
For **CLIENT_ID** and **CLIENT_SECRET** values paste those obtained from GitHub in *Installation Prerequisites* section.

**APP_SECRET** is the secret key for Flask app that should not be exposed. You can use the output of the below snippet to generate key or any other phrase of your choice:
```python
import os
os.urandom(24)
```
4. **This should not be done in prod!**
Normally OAuth2 is not used over HTTP, but it can be useful for local testing. In order to achieve that either set environment variable:
```bash
export OAUTHLIB_INSECURE_TRANSPORT=1
```
or uncomment the following line in *repl_app.py* file:
```python
 os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
```
5. Finally run the application:
```bash
python repl_app.py
```
6. Go to [http://127.0.0.1:5000](http://127.0.0.1:5000). If everything is done correctly you get the repository forked to your profile. Congrats!

## Heroku Installation
1. Login to Heroku and go [create new app](https://dashboard.heroku.com/new-app)
2. Give the name to your app in **App name** field. 
3. On the next page choose the **Deployment method** that works best for you.
4. On **Activity** tab expand **Config Vars** and set environment variables with your own values. Lookup their meaning in *Local Installation* section

```bash
CLIENT_ID=your_github_client_id
CLIENT_SECRET=your_github_client_secret
APP_SECRET=your_app_secret_id
```
5. Click on **Open app** in the top right corner of Heroku dashboard to check that you can successfully fork the repository. Congratulations!