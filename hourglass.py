#!/usr/bin/env python

# Chris Nyland
# 2020-04-01

# Flask backend to serve as a point counter for Ragnar and Gunnar

import sqlite3
from flask import Flask
from flask import request

dbfilename = 'hourglass.db' 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
    

@app.route('/api/add')
def addpoint():
    return '+1'
    
@app.route('/api/subtract')
def subtractpoint():
    return '-1'
    
@app.route('/api/user/add', methods=['POST'])
def adduser():
    query = 'insert into users (name, role) values (?, ?)'
    name = request.form['name']
    role = request.form['role']
    with sqlite3.connect(dbfilename) as con:
        cur = con.cursor()
        cur.execute(query, (name, role))
        cur.close()
        con.commit()
    return ''

@app.route('/api/award/<int:awardee>/<int:point_change>', methods=['POST'])
def award(awardee, point_change):
    query = 'insert into points (awarder, awardee, point_change) values (?, ?, ?)'
    with sqlite3.connect(dbfilename) as con:
        cur = con.cursor()
        cur.execute(query, (-1, awardee, point_change))
        cur.close()
        con.commit()
    return ''
