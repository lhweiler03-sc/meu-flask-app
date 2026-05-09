 })from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = []

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

@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify(usuarios)

@app.route("/api/users", methods=["POST"])
def add_user():
    data = request.json

    usuarios.append({
        "nome": data.get("nome")
    })

    return jsonify({
        "success": True,
        "usuarios": usuarios
    })

if __name__ == "__main__":
    app.run(debug=True)
