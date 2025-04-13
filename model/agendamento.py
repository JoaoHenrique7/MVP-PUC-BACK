from .base import db

class Agendamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_nome = db.Column(db.String(100), nullable=False)
    data_hora = db.Column(db.DateTime, nullable=False)
    barbeiro_id = db.Column(db.Integer, db.ForeignKey('barbeiro.id'), nullable=False)
    servico_id = db.Column(db.Integer, db.ForeignKey('servico.id'), nullable=False)

    barbeiro = db.relationship('Barbeiro')
    servico = db.relationship('Servico')

    def to_dict(self):
        return {
            "id": self.id,
            "cliente_nome": self.cliente_nome,
            "data_hora": self.data_hora.isoformat(),
            "barbeiro": self.barbeiro.to_dict(),
            "servico": self.servico.to_dict()
        }
