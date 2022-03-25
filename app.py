# import the framwework
from crypt import methods
from ntpath import join
from operator import methodcaller
from unittest.util import strclass
from flask import Flask, render_template, request
from flask import make_response
from datetime import datetime

# Create the application instance
app = Flask(__name__)

# Define a route and the function that will be executed
@app.route('/', methods=["GET"])
def index():
    return render_template("form.html")

# Define a route and the function that will be executed
@app.route('/', methods=["POST"])
def indexReturn():
    num = int(request.form.get('number'))
    list =[]
    ognum=num
    if (num%2)!=1:
        num=num-1
    else:
        num=num-2    
    ts =datetime.now()
    while num>1:
        if isPrime(num):
            list.append(num)
        num=num-2
    if (ognum>=2):
        list.append(2)
    t= datetime.now()
    d=t-ts
    h,m,s,ms=convert_timedelta(d)
    list.reverse()
    if len(list)>20:
        strList="The Last 10 Primes are "+", ".join(format(e, ',d') for e in list[-10:]) + " and the First 10 Primes are "+ ", ".join(format(e, ',d') for e in list[0:10])
    else:
        strList=", ".join(format(e, ',d') for e in list)
    return render_template('results.html',original=format(ognum, ',d'), text=strList, time="It took {} hours, {} minutes, {} seconds and {} microseconds to calculate all {} primes.".format(h,m,s,ms, format(len(list), ',d')))  
def isPrime(n):
    p = True
    if n > 1:
        for m in range(2, n):
            if n % m == 0:
                p = False
    return p
def convert_timedelta(duration):
    s=duration.seconds
    return int(s/3600),int(s/60),s,format(duration.microseconds, ',d')#h,m,s,ms
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