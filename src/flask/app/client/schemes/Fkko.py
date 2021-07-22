from marshmallow_sqlalchemy import ModelSchema
from app.models import Fkko
from app.client.schemes.FkkoClass import FkkoClassClientSchema
from app.client.schemes.Aggr import AggrClientSchema
from marshmallow import fields

class FkkoClientSchema(ModelSchema):
    fkkoclass = fields.Nested(FkkoClassClientSchema)
    aggr = fields.Nested(AggrClientSchema)
    codespace = fields.Method("getCodeSpace")
    class Meta:
        model = Fkko

    def getCodeSpace(self, el):
        return "{} {} {} {} {} {}".format(str(el.id)[0], str(el.id)[1:3], str(el.id)[3:6], str(el.id)[6:8], str(el.id)[8:10], str(el.id)[10])