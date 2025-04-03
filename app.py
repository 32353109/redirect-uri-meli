import requests
from flask import Flask, request
import os

app = Flask(__name__)

# Configurações (substitua pelos seus valores reais)
CLIENT_ID = os.getenv('CLIENT_ID', 'seu_client_id_aqui')
CLIENT_SECRET = os.getenv('CLIENT_SECRET', 'seu_client_secret_aqui')
REDIRECT_URI = os.getenv('REDIRECT_URI', 'https://seu-app.up.railway.app/oauth/callback')

@app.route('/oauth/callback')
def callback():
    code = request.args.get('code')
    if code:
        # Troca o código por tokens
        token_url = "https://api.mercadolibre.com/oauth/token"
        payload = {
            'grant_type': 'authorization_code',
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'code': code,
            'redirect_uri': REDIRECT_URI
        }
        response = requests.post(token_url, data=payload)
        
        if response.status_code == 200:
            return response.json()
    return "Erro na autenticação", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT', 8080))
