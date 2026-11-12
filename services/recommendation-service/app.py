from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/recommend/<int:age>', methods=['GET'])
def recommend(age):

    if age < 25:
        recommendation = "Vehicle Insurance"
    elif age < 50:
        recommendation = "Health Insurance"
    else:
        recommendation = "Life Insurance"

    return jsonify({
        "age": age,
        "recommendation": recommendation
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)