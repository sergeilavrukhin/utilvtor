from marshmallow_sqlalchemy import ModelSchema
from app.models import Region
from marshmallow import fields
import json

class RegionClientSchema(ModelSchema):
    value = fields.Method("getValue")
    activity = fields.Method("getActivity")

    class Meta:
        model = Region

    def getValue(self, el):
        return el.id

    def getActivity(self, el):
        return json.loads(el.activity)