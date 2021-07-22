from marshmallow_sqlalchemy import ModelSchema
from app.models import CompaniesWaste
from app.client.schemes.Fkko import FkkoClientSchema
from marshmallow import fields
import json

class CompanyWasteClientSchema(ModelSchema):
    fkko = fields.Nested(FkkoClientSchema, only=("id", "name", "codespace"))
    activity = fields.Method("getActivity")

    class Meta:
        model = CompaniesWaste

    def getActivity(self, el):
        if el.activity != None:
            return json.loads(el.activity)
        else:
            return None