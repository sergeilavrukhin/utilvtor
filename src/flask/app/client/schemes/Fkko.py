from marshmallow_sqlalchemy import ModelSchema
from app.models import Fkko, FkkoClass
from marshmallow import fields

class FkkoClassClientSchema(ModelSchema):
    class Meta:
        model = FkkoClass

class FkkoClientSchema(ModelSchema):
    fkkoclass = fields.Nested("FkkoClassClientSchema")
    class Meta:
        model = Fkko