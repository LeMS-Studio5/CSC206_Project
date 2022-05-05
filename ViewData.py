# import the framwework
from unittest.util import strclass
from flask import Flask, render_template, request
from flask import make_response
from datetime import datetime
from DB.db_connector import Athlete,DbConnector
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# Create the application instance
app = Flask(__name__)
@app.route('/', methods=["GET"])
def index():
    d=DbConnector(False)
    return render_template('tables.html',data=d.allContent(),header="Overall Ranks")
@app.route('/USA', methods=["GET"])
def USA():
    d=DbConnector(False)
    return render_template('tables.html',data=d.nationContent("USA"),header="USA Athletes")
@app.route('/21st', methods=["GET"])
def year():
    d=DbConnector(False)
    return render_template('tables.html',data=d.newerThanContent(1999),header="21st Century Athletes")
@app.route('/Salary', methods=["GET"])
def sal():
    d=DbConnector(False)
    mat1 = np.array(d.byRank(1))
    plt.xticks(ticks=range(len(mat1[:,6])), rotation=90)
    plt.ylabel("Earnings (in Millions of Dollars)")
    plt.xlabel("Years")
    plt.gcf().subplots_adjust(bottom=0.15)
    plt.title("Top Ranking Salary Increase")
    plt.plot(mat1[:, 6],mat1[:, 7])
    fig='static/myfig.png'
    plt.savefig(fig,dpi=150)
    plt.close()
    return render_template('graphs.html',fig=fig,title="Salary Increase")
@app.route('/Percent', methods=["GET"])
def Percent():
    d=DbConnector(False)
    mat1 = np.array(d.allContent())
    l=[]
    for m in mat1[:,5]:
        l.append(m.capitalize())
    plt.title("Percentage of Athletes per Sport")
    p=Counter(l)
    a=[]
    t=[]
    other=0
    for i in p:
        if (p[i]>len(l)*.02):
            t.append(i)
            a.append(p[i])
        else:
            other+=p[i]
    a.append(other)
    t.append("Other")
    plt.pie(a,labels=t)
    fig='static/myfig.png'
    plt.savefig(fig,dpi=150)
    plt.close()
    return render_template('graphs.html',fig=fig,title="Percentage of Athletes")
@app.route('/Cost', methods=["GET"])
def Cost():
    d=DbConnector(False)
    mat1 = np.array(d.allContent())
    sport={}
    for e in mat1:
        if e[5].capitalize() in sport:
            sport[e[5].capitalize()]+=float(e[7]);
        else:
            k=e[5].capitalize();
            sport[k]=float(e[7]);
    plt.title("Cost Each Sport Makes")
    plt.xticks(ticks=range(len(mat1[:,6])), rotation=90)
    plt.ylabel("Earnings (in Millions of Dollars)")
    plt.xlabel("Sport")
    plt.gcf().subplots_adjust(bottom=0.5)
    a=[]
    t=[]
    other=0
    for i in sport:
        t.append(i)
        a.append(sport[i])
    plt.plot(t,a)
    fig='static/myfig.png'
    plt.savefig(fig,dpi=150)
    plt.close()
    return render_template('graphs.html',fig=fig,title="Cost of Each Sport")
#   To run - in your WSL window type this:
#       export FLASK_APP=fwd_02.py
#       flask run
#
#   The export adds the name of your file to the environment
#   Fflask run will run the file specified by FLASK_APP in
#   a development web s`erver
#
#   demo grep, | and env
# Allows you to start the application by executing this file
# No need to export and flask run
# Debug mode - code reloading and exception display
if __name__ == '__main__':
    app.run(debug=True)