from marshmallow import Schema, fields

class AgendamentoSchema(Schema):
    id = fields.Int(dump_only=True)
    cliente_nome = fields.Str(required=True)
    data_hora = fields.DateTime(required=True)
    barbeiro_id = fields.Int(required=True)
    servico_id = fields.Int(required=True)
