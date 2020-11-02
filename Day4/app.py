from flask import Flask, jsonify
import json

app = Flask(__name__)

users_list = [

    {
        'userid' : 1,
        'username' : 'Jagriti',
        'skillid' : 2
    },
    {
        'userid' : 2,
        'username' : 'San',
        'skillid' : 2
    },
    {
        'userid' : 3,
        'username' : 'San',
        'skillid' : 2
    },
     {
        'userid' : 4,
        'username' : 'Space',
        'skillid' : 2
    },
]

skills_list = [

    {
        'skillid' : 1,
        'skillname' : 'Java'
    },
    {
        'skillid' : 2,
        'skillname' : 'Python'
    },
    {
        'skillid' : 3,
        'skillname' : 'C++'
    }
]
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users')
def users():
    return jsonify(users_list)

@app.route('/users/<int:userid>')
def user(userid):
    return jsonify(users_list[userid-1])

@app.route('/skills')
def skills():
    return jsonify(skills_list)

@app.route('/users/<int:userid>/skills')
def list_of_skills(userid):
    return jsonify(skills_list[userid-1])
    