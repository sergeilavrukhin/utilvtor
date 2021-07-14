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
        if isinstance(el, dict):
            return el['id']
        else:
            return el.id

    def getActivity(self, el):
        return json.loads(el.activity)