from marshmallow import Schema, fields, validate


class ItemSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True, validate=validate.Length(min=3, max=50, error='Input "{input}" length must be between {min} and {max}'))
    groups = fields.Nested('GroupSchema', many=True, exclude=('items', ))