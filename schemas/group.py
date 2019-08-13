from marshmallow import Schema, fields, validate


class GroupSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True, validate=validate.Length(min=3, max=50, error='Input "{input}" length must be between {min} and {max}'))
    description = fields.Str(required=False, validate=validate.Length(max=50, error='Input "{input}" length must be less than {max}'))
    items = fields.Nested('ItemSchema', many=True, exclude=('groups', ))
