from flask import Flask, jsonify, request
from api.funcao_link import webscrap, webscrap_title
from flasgger import Swagger
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)

auth = HTTPBasicAuth()

USERS = {
  "admin": "admin",
  "user":"senha"
}

swagger = Swagger(app)

@auth.verify_password
def verify_password(username, password):
  if username in USERS and USERS[username] == password:
    return username
  return None

@app.route('/')
#@auth.login_required
def home():
    return "Bem vindo a Embrapa-API"



@app.route('/titulo', methods=['GET'])
#@auth.login_required

def titulo():
    """
    Extrai cabeçalho de uma pagina URL.
    ---
    security:
      - BasicAuth: []
    parameters:
      - name: url
        in: query
        type: string
        required: true
        description: URL da página web para extrair o conteúdo.
      - name: token
        in: query
        type: string
        required: true
        description: Token de acesso.
    responses:
      200:
        description: Conteúdo da página web.
        schema:
          type: object
          properties:
            headers:
              type: array
              items:
                type: string
              description: Lista de cabeçalhos (h1, h2, h3).
            paragraphs:
              type: array
              items:
                type: string
              description: Lista de parágrafos.
      400:
        description: Erro de requisição.
      401:
        description: Não autorizado.
    """
    site = request.args.get('url')
    token = request.args.get('token')

    if token!= "token_valido":
        return jsonify({"message": "Token inválido"}), 401
    else:
       df = webscrap_title(site)
    
       return jsonify(df)



@app.route('/conteudo', methods=['GET'])
#@auth.login_required

def conteudo():
    """
    Extrai  parágrafos de uma página web fornecida pela URL.
    ---
    security:
      - BasicAuth: []
    parameters:
      - name: url
        in: query
        type: string
        required: true
        description: URL da página web para extrair o conteúdo.
      - name: token
        in: query
        type: string
        required: true
        description: Token de acesso.
    responses:
      200:
        description: Conteúdo da página web.
        schema:
          type: object
          properties:
            headers:
              type: array
              items:
                type: string
              description: Lista de cabeçalhos (h1, h2, h3).
            paragraphs:
              type: array
              items:
                type: string
              description: Lista de parágrafos.
      400:
        description: Erro de requisição.
      401:
        description: Não autorizado.
    """
    site = request.args.get('url')
    token = request.args.get('token')

    if token!= "token_valido":
        return jsonify({"message": "Token inválido"}), 401
    else:
      df = webscrap(site)
      df_dict = df.to_dict(orient = 'records')
      return jsonify(df_dict)




if __name__ == '__main__':
    app.run(debug=True)

