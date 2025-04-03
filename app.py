import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/oauth/callback')
def callback():
    code = request.args.get('code')
    
    if code:
        print(f"Código de autorização recebido: {code}")  # Exibe no terminal do Railway
        return "Código recebido com sucesso! Pode fechar esta página."
    else:
        return "Erro: Código de autorização não recebido.", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
