#! /usr/bin/python
'''
    Web Service for Simple Superhero Voting Application

    This is the Web Service for a basic microservice demo application.
    The application was designed to provide a simple demo for Cisco Mantl

'''

from flask import Flask, render_template, request, jsonify
import datetime
import urllib
import json
import os

app = Flask(__name__)

@app.route("/")
def template_test():
    # Check for submitted vote
    vote = request.args.get('hero')
    if (vote):
        v = urllib.urlopen(app_server + "/vote/" + vote)

    u = urllib.urlopen(app_server + "/hero_list")
    page = u.read()
    hero_list = json.loads(page)["heros"]
    return render_template('home.html', hero_list=hero_list, title="Microservice Demo Application", current_time=datetime.datetime.now())

@app.route("/about")
def about():
    return render_template('about.html', title="About", current_time=datetime.datetime.now())

@app.route("/results")
def results():
    # Check for submitted vote
    vote = request.args.get('hero')
    if (vote):
        v = urllib.urlopen(app_server + "/vote/" + vote)

    u = urllib.urlopen(app_server + "/results")
    page = u.read()
    tally = json.loads(page)
    tally = sorted(tally.items(), key = lambda (k,v): v, reverse=True)
    return render_template('results.html', tally = tally, title="Results", current_time=datetime.datetime.now())

@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    """convert a datetime to a different format."""
    return value.strftime(format)

app.jinja_env.filters['datetimefilter'] = datetimefilter

if __name__=='__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser("MyHero Web Service")
    parser.add_argument(
        "-a", "--app", help="Address of app server", required=False
    )
    args = parser.parse_args()

    app_server = args.app
    # print "Arg App: " + str(app_server)
    if (app_server == None):
        app_server = os.getenv("myhero_app_server")
        # print "Env App: " + str(app_server)
        if (app_server == None):
            get_app_server = raw_input("What is the app server address? ")
            # print "Input App: " + str(get_app_server)
            app_server = get_app_server

    print "App Server: " + app_server

    app.run(debug=True, host='0.0.0.0', port=int("5000"))


