import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/oauth/callback')
def callback():
    code = request.args.get('code')
    if code:
        print(f"Código de autorização recebido: {code}")
        return jsonify({"code": code})  # Retorna o código no corpo da resposta
    else:
        return jsonify({"error": "Código de autorização não recebido"}), 400

@app.route('/')
def home():
    return "Servidor de redirecionamento do Mercado Livre."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))  # Mantendo a porta 8080
