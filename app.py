import os
import requests
from flask import Flask, request, jsonify
from urllib.parse import quote

app = Flask(__name__)

# Configurações (substitua ou use variáveis de ambiente)
CLIENT_ID = os.getenv('CLIENT_ID', '1200469458018603')
CLIENT_SECRET = os.getenv('CLIENT_SECRET', 'd6Osja9ZvaXDj9QqZfUeTDfOegr6RbnO')
REDIRECT_URI = os.getenv('REDIRECT_URI', 'https://redirect-uri-meli.up.railway.app/oauth/callback')

# Rota para iniciar o fluxo OAuth
@app.route('/auth')
def auth():
    auth_url = (
        f"https://auth.mercadolivre.com.br/authorization"
        f"?response_type=code"
        f"&client_id={CLIENT_ID}"
        f"&redirect_uri={quote(REDIRECT_URI)}"
    )
    return redirect(auth_url)

# Rota de callback
@app.route('/oauth/callback')
def callback():
    code = request.args.get('code')
    if not code:
        return jsonify({"error": "Código de autorização não fornecido"}), 400
    
    # Troca o código pelos tokens
    token_url = "https://api.mercadolibre.com/oauth/token"
    payload = {
        'grant_type': 'authorization_code',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': code,
        'redirect_uri': REDIRECT_URI
    }
    
    try:
        response = requests.post(token_url, data=payload)
        if response.status_code == 200:
            tokens = response.json()
            # Aqui você pode salvar os tokens no banco de dados ou variáveis de ambiente
            return jsonify({
                "message": "Autenticação bem-sucedida",
                "tokens": {
                    "access_token": tokens['access_token'],
                    "refresh_token": tokens['refresh_token'],
                    "expires_in": tokens['expires_in']
                }
            })
        else:
            return jsonify({
                "error": "Falha ao obter tokens",
                "details": response.json()
            }), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return "Servidor OAuth do Mercado Livre - Use /auth para iniciar o fluxo"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
