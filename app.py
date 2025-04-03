import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/oauth/callback')
def callback():
    code = request.args.get('code')
    full_url = request.url  # Captura a URL completa da requisição
    
    if code:
        print(f"URL completa: {full_url}")  # Exibe a URL gerada no terminal
        print(f"Código de autorização recebido: {code}")
        return "Código recebido com sucesso! Pode fechar esta página."
    else:
        return "Erro: Código de autorização não recebido.", 400

@app.route('/')
def home():
    return "Bem-vindo ao servidor de redirecionamento!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))  # Usa a porta 8080 conforme sua configuração
