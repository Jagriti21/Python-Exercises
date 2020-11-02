from flask import Flask, request, jsonify

app = Flask(__name__)

developers = {
    1: { "name": "john", "skills": ["python", "aws"]},
    2: { "name": "jane", "skills": ["java", "jsp"] },
    3: { "name": "james", "skills": ["python", "ml"] },
    4: { "name": "jack", "skills": ["python", "ds"] },
    5: { "name": "jill", "skills": ["go", "web"] },
}

@app.route('/')
def index():
    return "Home Page of the API"

@app.route('/developers/<int:dev_id>', methods=['PUT', 'GET', 'DELETE'])
def dev(dev_id):
    dev = developers.get(dev_id)
    if not dev:
        return jsonify("Developer not found"), 404
    else:
        if request.method == 'PUT':
            new_dev = request.json
            developers[dev_id] = new_dev
            return f"{dev_id} was updated", 200
        elif request.method == 'DELETE':
            del developers[dev_id]
            return f"{dev_id} was deleted", 204
        else:
            return dev

@app.route('/developers/', methods=['POST', 'GET'])
def devs():
    print(request.method)
    if request.method == 'POST': 
        new_dev = request.json
        new_dev_id = max(developers) + 1
        developers[new_dev_id] = new_dev
        return developers[new_dev_id], 201
    else: 
        return developers, 200