from marshmallow_sqlalchemy import ModelSchema
from app.models import Unit
from marshmallow import fields

class UnitClientSchema(ModelSchema):
    value = fields.Method("getValue")
    class Meta:
        model = Unit

    def getValue(self, el):
        return el.id