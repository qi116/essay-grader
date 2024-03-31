from flask import Flask, jsonify, request
from flask_cors import CORS 
from model.model import evaluate, load_model

app = Flask(__name__)
CORS(app)

model = load_model('model/model.tp')

@app.route("/api/python/", methods=["GET"])
def hello_world():
    return jsonify({'message': 'Hello from Flask!'})

@app.route("/api/request/", methods=["GET", "POST"])
def send_msg():
    content = request.get_json()['postContent']
    score_tensor = evaluate(model, content)
    score = score_tensor.item()
    print(score)
    return jsonify({'message': round(score, 2)})

 

if __name__ == '__main__':
    app.run(debug=True, port=8080)