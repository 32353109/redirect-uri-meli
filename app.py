import os
import requests
from flask import Flask, request

app = Flask(__name__)

LOCAL_SERVER_URL = "http://localhost:5001/receive_code"  # Seu script local receberá o código aqui

@app.route('/oauth/callback', methods=['GET', 'POST'])
def callback():
    if request.method == 'GET':  # O código só chega via GET
        code = request.args.get('code')
        if code:
            print(f"Código de autorização recebido: {code}")

            # ✅ Envia automaticamente o código para seu script local
            try:
                requests.post(LOCAL_SERVER_URL, json={"code": code}, timeout=5)
            except requests.exceptions.RequestException as e:
                print(f"Erro ao enviar código para o script local: {e}")

            return "Código recebido com sucesso!"
        else:
            return "Erro: Código de autorização não recebido.", 400

    elif request.method == 'POST':  # Apenas evita erro 405
        return "Método POST recebido, mas ignorado.", 200

@app.route('/')
def home():
    return "Servidor de redirecionamento Mercado Livre."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))  # Porta 8080 no Railway
