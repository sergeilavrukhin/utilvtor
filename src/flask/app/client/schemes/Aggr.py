from marshmallow_sqlalchemy import ModelSchema
from app.models import Aggregation
from marshmallow import fields

class AggrClientSchema(ModelSchema):
    value = fields.Method("getValue")
    class Meta:
        model = Aggregation

    def getValue(self, el):
        return el.id