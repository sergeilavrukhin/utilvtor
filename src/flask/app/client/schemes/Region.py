from marshmallow_sqlalchemy import ModelSchema
from app.models import Region
from marshmallow import fields

class RegionClientSchema(ModelSchema):
    value = fields.Method("getValue")
    class Meta:
        model = Region

    def getValue(self, el):
        return el.id