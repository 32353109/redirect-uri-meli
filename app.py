import os
import requests
from flask import Flask, request

app = Flask(__name__)

LOCAL_SERVER_URL = "http://localhost:5001/receive_code"  # Seu script Python rodará aqui

@app.route('/oauth/callback')
def callback():
    code = request.args.get('code')
    full_url = request.url  # Captura a URL completa da requisição
    
    if code:
        print(f"URL completa: {full_url}")  # Exibe a URL gerada no terminal do Railway
        print(f"Código de autorização recebido: {code}")
        
        # Envia o código para o script local
        try:
            requests.post(LOCAL_SERVER_URL, json={"code": code})
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar código para o script local: {e}")
        
        return "Código recebido com sucesso! Pode fechar esta página."
    else:
        return "Erro: Código de autorização não recebido.", 400

@app.route('/')
def home():
    return "Bem-vindo ao servidor de redirecionamento!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))  # Usa a porta 8080 conforme sua configuração
