from flask import Flask, jsonify

app = Flask(__name__)

claims = [
    {
        "id": 1,
        "userId": 1,
        "policyId": 1,
        "amount": 20000,
        "status": "Approved"
    }
]

@app.route('/claims', methods=['GET'])
def get_claims():
    return jsonify(claims)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)