# import the framwework
from crypt import methods
from email import header
from ntpath import join
from operator import methodcaller
from unittest.util import strclass
from flask import Flask, render_template, request
from flask import make_response
from datetime import datetime
from DB.db_connector import Athlete,DbConnector

# Create the application instance
app = Flask(__name__)
@app.route('/', methods=["GET"])
def index():
    d=DbConnector(False)
    return render_template('graphs.html',data=d.allContent(),header="Overall Ranks")
@app.route('/USA', methods=["GET"])
def USA():
    d=DbConnector(False)
    return render_template('graphs.html',data=d.nationContent("USA"),header="USA Athletes")
@app.route('/21st', methods=["GET"])
def year():
    d=DbConnector(False)
    return render_template('graphs.html',data=d.newerThanContent(1999),header="21st Century Athletes")
#   To run - in your WSL window type this:
#       export FLASK_APP=fwd_02.py
#       flask run
#
#   The export adds the name of your file to the environment
#   Fflask run will run the file specified by FLASK_APP in
#   a development web server
#
#   demo grep, | and env
# Allows you to start the application by executing this file
# No need to export and flask run
# Debug mode - code reloading and exception display
if __name__ == '__main__':
    app.run(debug=True)