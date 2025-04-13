from marshmallow import Schema, fields

class BarbeiroSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
