from flask import Flask, request, jsonify
from flasgger import Swagger
from model.base import db
from model.barbeiro import Barbeiro
from model.servico import Servico
from model.agendamento import Agendamento
from schemas.barbeiro import BarbeiroSchema
from schemas.servico import ServicoSchema
from schemas.agendamento import AgendamentoSchema
from logger import logger
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///barbearia.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Configuração do Swagger
swagger = Swagger(app)

# ---- Rotas Barbeiro ----
@app.route('/barbeiros', methods=['POST'])
def criar_barbeiro():
    """
    Cria um novo barbeiro
    ---
    tags:
      - Barbeiros
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: Barbeiro
          required:
            - nome
          properties:
            nome:
              type: string
              description: Nome do barbeiro
    responses:
      201:
        description: Barbeiro criado com sucesso
    """
    data = request.json
    barbeiro = Barbeiro(nome=data['nome'])
    db.session.add(barbeiro)
    db.session.commit()
    return BarbeiroSchema().dump(barbeiro), 201

@app.route('/barbeiros', methods=['GET'])
def listar_barbeiros():
    """
    Lista todos os barbeiros
    ---
    tags:
      - Barbeiros
    responses:
      200:
        description: Lista de barbeiros
    """
    barbeiros = Barbeiro.query.all()
    return BarbeiroSchema(many=True).dump(barbeiros), 200

# ---- Rotas Serviço ----
@app.route('/servicos', methods=['POST'])
def criar_servico():
    """
    Cria um novo serviço
    ---
    tags:
      - Serviços
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: Servico
          required:
            - nome
            - preco
          properties:
            nome:
              type: string
              description: Nome do serviço
            preco:
              type: number
              format: float
              description: Preço do serviço
    responses:
      201:
        description: Serviço criado com sucesso
    """
    data = request.json
    servico = Servico(nome=data['nome'], preco=data['preco'])
    db.session.add(servico)
    db.session.commit()
    return ServicoSchema().dump(servico), 201

@app.route('/servicos', methods=['GET'])
def listar_servicos():
    """
    Lista todos os serviços
    ---
    tags:
      - Serviços
    responses:
      200:
        description: Lista de serviços
    """
    servicos = Servico.query.all()
    return ServicoSchema(many=True).dump(servicos), 200

# ---- Rotas Agendamento ----
@app.route('/agendamentos', methods=['POST'])
def criar_agendamento():
    """
    Cria um novo agendamento
    ---
    tags:
      - Agendamentos
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: Agendamento
          required:
            - barbeiro_id
            - servico_id
            - data_hora
          properties:
            barbeiro_id:
              type: integer
            servico_id:
              type: integer
            data_hora:
              type: string
              format: date-time
              description: Data e hora do agendamento (YYYY-MM-DD HH:MM:SS)
    responses:
      201:
        description: Agendamento criado com sucesso
    """
    data = request.json
    data_hora = datetime.strptime(data['data_hora'], '%Y-%m-%d %H:%M:%S')
    agendamento = Agendamento(
        barbeiro_id=data['barbeiro_id'],
        servico_id=data['servico_id'],
        data_hora=data_hora
    )
    db.session.add(agendamento)
    db.session.commit()
    return AgendamentoSchema().dump(agendamento), 201

@app.route('/agendamentos', methods=['GET'])
def listar_agendamentos():
    """
    Lista todos os agendamentos
    ---
    tags:
      - Agendamentos
    responses:
      200:
        description: Lista de agendamentos
    """
    agendamentos = Agendamento.query.all()
    return AgendamentoSchema(many=True).dump(agendamentos), 200

# ---- Rodar o servidor ----
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
