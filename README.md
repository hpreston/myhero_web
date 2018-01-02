**This is the original Web Service for the MyHero application.  Though it still work and can be used, a newer option [myhero_ui](https://github.com/hpreston/myhero_ui) has been developed that provides a much better user experience.  It is recommended that users leverage the new interface moving forward.**

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
* UI - [hpreston/myhero_ui](https://github.com/hpreston/myhero_ui)
* Ernst - [hpreston/myhero_ernst](https://github.com/hpreston/myhero_ernst)
  * Optional Service used along with an MQTT server when App is in "queue" mode
* Spark Bot - [hpreston/myhero_spark](https://github.com/hpreston/myhero_spark)
  * Optional Service that allows voting through IM/Chat with a Cisco Spark Bot
* Tropo App - [hpreston/myhero_tropo](https://github.com/hpreston/myhero_tropo)
  * Optional Service that allows voting through TXT/SMS messaging


The docker containers are available at

* Data - [hpreston/myhero_data](https://hub.docker.com/r/hpreston/myhero_data)
* App - [hpreston/myhero_app](https://hub.docker.com/r/hpreston/myhero_app)
* Web - [hpreston/myhero_web](https://hub.docker.com/r/hpreston/myhero_web)
* UI - [hpreston/myhero_ui](https://hub.docker.com/r/hpreston/myhero_ui)* Ernst - [hpreston/myhero_ernst](https://hub.docker.com/r/hpreston/myhero_ernst)
  * Optional Service used along with an MQTT server when App is in "queue" mode
* Spark Bot - [hpreston/myhero_spark](https://hub.docker.com/r/hpreston/myhero_spark)
  * Optional Service that allows voting through IM/Chat with a Cisco Spark Bot
* Tropo App - [hpreston/myhero_tropo](https://hub.docker.com/r/hpreston/myhero_tropo)
  * Optional Service that allows voting through TXT/SMS messaging

## Basic Application Details

Required

* flask
* ArgumentParser
* requests

# Environment Installation

    pip install -r requirements.txt

# Basic Usage

In order to run, the service needs 2 pieces of information to be provided:

* App Server Address
* App Server Authentication Key to Use

These details can be provided in one of three ways.

* As a command line argument
  - `python myhero_web/myhero_web.py --app "http://myhero-web.server.com" --appkey "APP AUTH KEY" `
* As environment variables
  - `export myhero_app_server="http://myhero-app.server.com"`
  - `export myhero_app_key="APP AUTH KEY"`
  - `python myhero_web/myhero_web.py`
* As raw input when the application is run
  - `python myhero_web/myhero_web.py`
  - `What is the app server address? http://myhero-app.server.com`
  - `App Server Key: APP AUTH KEY`

A command line argument overrides an environment variable, and raw input is only used if neither of the other two options provide needed details.


# Accessing

    http://localhost:5000/

# Local Development with Vagrant

I've included the configuration files needed to do local development with Vagrant in the repo.  Vagrant will still use Docker for local development and is configured to spin up a CentOS7 host VM for running the container.

To start local development run:

* `vagrant up`
  * You may need to run this twice.  The first time to start the docker host, and the second to start the container.
* Now you can interact with the API or interface at localhost:15002 (configured in Vagrantfile and Vagrantfile.host)
  * example:  from your local machine open http://localhost:15002 in a web browser
  * Environment Variables are configured in Vagrantfile for development

Each of the services in the application (i.e. myhero_web, myhero_app, and myhero_data) include Vagrant support to allow working locally on all three simultaneously.
