from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "message": "API funcionando"
    })

@app.route("/api/test")
def test():
    return jsonify({
        "success": True,
        "data": "Olá do Flask"
    })
