from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)


app.config['MONGO_DBNAME'] = 'demo'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/demo'


mongo = PyMongo(app)

'''
bank_users = {
    1: { "username": "john", "password": "john1" },
    2: { "username": "jane", "password": "jane1" },
    3: { "username": "james", "password": "james1" },
    4: { "username": "jack", "password": "jack1" },
    5: { "username": "jill", "password": "jill1"},
}
'''

@app.route('/')
def index():
    return "Banking Management System"

@app.route('/bank_users', methods=['GET'])
def get_all_users():
  user = mongo.db.users
  output = []
  for u in user.find():
    output.append({'username' : u['username'], 'password' : u['password']})
  return jsonify({'result' : output})

 

@app.route('/bank_users/', methods=['GET'])
def get_one_user(username):
  user = mongo.db.users
  u = user.find_one({'username' : username})
  if u:
    output = {'username' : u['username'], 'password' : u['password']}
  else:
    output = "No such name"
  return jsonify({'result' : output})



   # else:
        
        #uname = bank_users[uid]['username'] #to fetch username for url userid
        #pwd= bank_users[uid]['password']   #to fetch password for url userid

         # condition to match if entered password == fetched password from db then allow login
         
        #return jsonify(f'hi {uname} welcome to loan page'),200


@app.route('/bank_users', methods=['POST'])
def add_user():
    user = mongo.db.users
    username = request.json['username']
    password = request.json['password']
    user_id = user.insert({'username': username, 'password': password})
    new_user = user.find_one({'_id': user_id })
    output = {'username' : new_user['username'], 'password' : new_user['password']}
    return jsonify({'result' : output})


if __name__ == '__main__':
    app.run(debug=True)
 