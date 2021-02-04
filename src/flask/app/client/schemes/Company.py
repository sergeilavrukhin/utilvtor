from marshmallow_sqlalchemy import ModelSchema
from app.models import Companies
from marshmallow import fields
import json

class CompanyClientSchema(ModelSchema):
    value = fields.Method("getValue")
    activity = fields.Method("getActivity")
    gps = fields.Method("getGPS")

    class Meta:
        model = Companies

    def getValue(self, el):
        return el.id

    def getActivity(self, el):
        if el.activity != None:
            return json.loads(el.activity)
        else:
            return None

    def getGPS(self, el):
        if el.gps != None:
            return json.loads(el.gps)
        else:
            return None