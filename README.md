# MyHero Web Service

This is the Web Service for a basic microservice demo application.
This provides a web front end into a voting system where users can vote for their favorite movie superhero.

Details on deploying the entire demo to a Mantl cluster can be found at
* MyHero Demo - [hpreston/myhero_demo](https://github.com/hpreston/myhero_demo)

The application was designed to provide a simple demo for Cisco Mantl.  It is written as a simple Python Flask application and deployed as a docker container.

Other services are:
* Data - [hpreston/myhero_data](https://github.com/hpreston/myhero_data)
* App - [hpreston/myhero_app](https://github.com/hpreston/myhero_app)
* Web - [hpreston/myhero_web](https://github.com/hpreston/myhero_web)

The docker containers are available at
* Data - [hpreston/myhero_data](https://hub.docker.com/r/hpreston/myhero_data)
* App - [hpreston/myhero_web](https://hub.docker.com/r/hpreston/myhero_app)
* Web - [hpreston/myhero_web](https://hub.docker.com/r/hpreston/myhero_web)

## Basic Application Details

Required

* flask
* ArgumentParser
* requests

# Installation

    pip install -r requirements.txt

# Usage

    python myhero_web/myhero_web.py -a http://APPSERVER-ADDRESS

In order to run, the service needs 2 pieces of information to be provided:
1. App Server Address
2. App Server Authentication Key to Use

These details can be provided in one of three ways.
1. As a command line argument
    - `python myhero_web/myhero_web.py --app "http://myhero-web.server.com" --appkey "APP AUTH KEY" `
2. As environment variables
    - `export myhero_app_server="http://myhero-app.server.com"`
    - `export myhero_app_key="APP AUTH KEY"`
    - `python myhero_web/myhero_web.py`
3. As raw input when the application is run
    - `python myhero_web/myhero_web.py`
    - `What is the app server address? http://myhero-app.server.com`
    - `App Server Key: APP AUTH KEY`

A command line argument overrides an environment variable, and raw input is only used if neither of the other two options provide needed details.


# Accessing

    http://localhost:5000/