from marshmallow_sqlalchemy import ModelSchema
from app.models import Fkko
from app.client.schemes.FkkoClass import FkkoClassClientSchema
from app.client.schemes.Aggr import AggrClientSchema
from marshmallow import fields

class FkkoClientSchema(ModelSchema):
    fkkoclass = fields.Nested(FkkoClassClientSchema)
    aggr = fields.Nested(AggrClientSchema)
    class Meta:
        model = Fkko