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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///barbearia.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
swagger = Swagger(app)

@app.before_first_request
def create_tables():
    db.create_all()

# Rotas Barbeiro
@app.route('/barbeiros', methods=['POST'])
def criar_barbeiro():
    """Cria um novo barbeiro"""
    data = request.json
    barbeiro = Barbeiro(nome=data['nome'])
    db.session.add(barbeiro)
    db.session.commit()
    return BarbeiroSchema().dump(barbeiro), 201

@app.route('/barbeiros', methods=['GET'])
def listar_barbeiros():
    barbeiros = Barbeiro.query.all()
    return BarbeiroSchema(many=True).dump(barbeiros), 200

# Rotas Serviço
@app.route('/servicos', methods=['POST'])
def criar_servico():
    """Cria um novo serviço"""
    data = request.json
    servico = Servico(nome=data['nome'], preco=data['preco'])
    db.session.add(servico)
    db.session.commit()
    return ServicoSchema().dump(servico), 201

@app.route('/servicos', methods=['GET'])
def listar_servicos():
    servicos = Servico.query.all()
    return ServicoSchema(many=True).dump(servicos), 200

# Rotas Agendamento
@app.route('/agendamentos', methods=['POST'])
def criar_agendamento():
    """Cria um novo agendamento"""
    data = request.json
    agendamento = Agendamento(
        cliente_nome=data['cliente_nome'],
        data_hora=datetime.fromisoformat(data['data_hora']),
        barbeiro_id=data['barbeiro_id'],
        servico_id=data['servico_id']
    )
    db.session.add(agendamento)
    db.session.commit()
    return AgendamentoSchema().dump(agendamento), 201

@app.route('/agendamentos', methods=['GET'])
def listar_agendamentos():
    agendamentos = Agendamento.query.all()
    return AgendamentoSchema(many=True).dump(agendamentos), 200

if __name__ == "__main__":
    app.run(debug=True)
