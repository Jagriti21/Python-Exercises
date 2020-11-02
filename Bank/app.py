from flask import Flask, request, jsonify

app = Flask(__name__)

bank_users = {
    1: { "username": "john", "password": "john1" },
    2: { "username": "jane", "password": "jane1" },
    3: { "username": "james", "password": "james1" },
    4: { "username": "jack", "password": "jack1" },
    5: { "username": "jill", "password": "jill1"},
}

@app.route('/')
def index():
    return "Banking Management System"

@app.route('/bank_users/<int:uid>', methods=[ 'GET'])
def login(uid):
    user = bank_users.get(uid)
   
    if not user:
        return jsonify("user not found."), 404
      
    else:
        uname = bank_users[uid]['username'] #to fetch username for url userid
        pwd= bank_users[uid]['password']   #to fetch password for url userid

         # condition to match if entered password == fetched password from db then allow login
         
        return jsonify(f'hi {uname} welcome to loan page'),200


