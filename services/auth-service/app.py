from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    users.append(data)
    return jsonify({
        "message": "User Registered Successfully"
    })

@app.route('/login', methods=['POST'])
def login():
    return jsonify({
        "message": "Login Successful"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)