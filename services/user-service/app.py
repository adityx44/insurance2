from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {
        "id": 1,
        "name": "Gayatri"
    },
    {
        "id": 2,
        "name": "User2"
    }
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)