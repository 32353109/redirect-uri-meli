import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/oauth/callback', methods=['GET', 'POST'])
def callback():
    if request.method == 'GET':  # Apenas GET tem o código de autorização
        code = request.args.get('code')
        if code:
            print(f"Código de autorização recebido: {code}")
            return "Código recebido com sucesso!"
        else:
            return "Erro: Código de autorização não recebido.", 400

    elif request.method == 'POST':  # Apenas evita o erro 405
        return "Método POST recebido, mas ignorado.", 200

@app.route('/')
def home():
    return "Servidor de redirecionamento Mercado Livre."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))  # Mantendo a porta 8080
