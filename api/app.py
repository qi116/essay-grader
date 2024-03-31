from flask import Flask, jsonify, request
from flask_cors import CORS 


app = Flask(__name__)
CORS(app)

@app.route("/api/python/", methods=["GET"])
def hello_world():
    return jsonify({'message': 'Hello from Flask!'})

@app.route("/api/request/", methods=["GET", "POST"])
def send_msg():
    print(request.get_json()["essay"])
    return jsonify({'message': request.get_json()["essay"]})



if __name__ == '__main__':
    app.run(debug=True)