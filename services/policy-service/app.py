from flask import Flask, jsonify

app = Flask(__name__)

policies = [
    {
        "id": 1,
        "name": "Health Insurance",
        "premium": 5000
    },
    {
        "id": 2,
        "name": "Life Insurance",
        "premium": 10000
    }
]

@app.route('/policies', methods=['GET'])
def get_policies():
    return jsonify(policies)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)