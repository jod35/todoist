from marshmallow import fields ,Schema

class TodoSchema(Schema):
    id=fields.Int()
    name=fields.Str()
    desc=fields.Str()
    priority=fields.Str()
    time=fields.DateTime()
    complete=fields.Bool()