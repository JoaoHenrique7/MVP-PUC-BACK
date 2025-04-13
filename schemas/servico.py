from marshmallow import Schema, fields

class ServicoSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    preco = fields.Float(required=True)
