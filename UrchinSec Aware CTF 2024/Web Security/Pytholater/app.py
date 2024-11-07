from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/routes', methods=['GET'])
def index():
    routes = {
        "addition": "/api/pytholator/add",
        "subtraction": "/api/pytholator/subtract",
        "multiplication": "/api/pytholator/multiply",
        "division": "/api/pytholator/divide",
        "magicball": "/api/pytholator/magicball"
    }
    return jsonify(routes)

@app.route('/api/pytholator/add', methods=['POST', 'GET'])
def addition():
    if request.method == 'POST':
        data = request.get_json()
        if not data['x']:
            return jsonify({"Error": "You did not provide the value of 'x'"}), 400
        elif not data['y']:
            return jsonify({"Error": "You did not provide the value of 'y'"}), 400
        elif data['x'] and data['y']:
            print(data['x'])
            print(data['y'])
            game = data['x'] + data['y']
            operation = eval(game)
            return jsonify({"Answer": operation})
        else:
            return jsonify({"Error": "Something Went Wrong"}), 500
    elif request.method == 'GET':
        return jsonify({"Error": "What Are You Trying To Do?"})

@app.route('/api/pytholator/subtract', methods=['POST', 'GET'])
def subtraction():
    if request.method == 'POST':
        data = request.get_json()
        if not data['x']:
            return jsonify({"Error": "You did not provide the value of 'x'"}), 400
        elif not data['y']:
            return jsonify({"Error": "You did not provide the value of 'y'"}), 400
        elif data['x'] and data['y']:
            operation = int(data['x']) - int(data['y'])
            return jsonify({"Answer": operation})
        else:
            return jsonify({"Error": "Something Went Wrong"}), 500
    elif request.method == 'GET':
        return jsonify({"Error": "What Are You Trying To Do?"})

@app.route('/api/pytholator/multiply', methods=['POST', 'GET'])
def multiplication():
    if request.method == 'POST':
        data = request.get_json()
        if not data['x']:
            return jsonify({"Error": "You did not provide the value of 'x'"}), 400
        elif not data['y']:
            return jsonify({"Error": "You did not provide the value of 'y'"}), 400
        elif data['x'] and data['y']:
            operation = int(data['x']) * int(data['y'])
            return jsonify({"Answer": operation})
        else:
            return jsonify({"Error": "Something Went Wrong"}), 500
    elif request.method == 'GET':
        return jsonify({"Error": "What Are You Trying To Do?"})

@app.route('/api/pytholator/divide', methods=['POST', 'GET'])
def division():
    if request.method == 'POST':
        data = request.get_json()
        if not data['x']:
            return jsonify({"Error": "You did not provide the value of 'x'"}), 400
        elif not data['y']:
            return jsonify({"Error": "You did not provide the value of 'y'"}), 400
        elif data['x'] and data['y']:
            operation = int(data['x']) / int(data['y'])
            return jsonify({"Answer": operation})
        else:
            return jsonify({"Error": "Something Went Wrong"}), 500
    elif request.method == 'GET':
        return jsonify({"Error": "What Are You Trying To Do?"})

@app.route('/api/pytholator/magicball', methods=['GET', 'POST'])
def magicball():
    return jsonify({"Note": "Are you sure this is the path you choose?"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)