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

# Installation

    pip install -r requirements.txt

# Usage

    python myhero_web/myhero_web.py -a http://APPSERVER-ADDRESS

# Accessing

    http://localhost:5000/