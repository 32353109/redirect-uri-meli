import os
from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/oauth/callback')
def callback():
    code = request.args.get('code')
    if code:
        print(f"Código de autorização recebido: {code}")
        return "Código recebido com sucesso!"
    else:
        return "Erro: Código de autorização não recebido.", 400

@app.route('/')
def home():
    return "Bem-vindo ao servidor de redirecionamento!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
