import os
from flask import Flask, request
import requests

app = Flask(__name__)

# Configurações via variáveis de ambiente
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')

@app.route('/callback')
def callback():
    code = request.args.get('code')
    if code:
        tokens = requests.post(
            "https://api.mercadolibre.com/oauth/token",
            data={
                "grant_type": "authorization_code",
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "code": code,
                "redirect_uri": REDIRECT_URI
            }
        ).json()
        
        # Aqui você pode salvar os tokens ou processá-los
        return f"Token recebido: {tokens.get('access_token')}"
    return "Erro: código não recebido", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 8080)))
