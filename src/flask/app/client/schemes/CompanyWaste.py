from marshmallow_sqlalchemy import ModelSchema
from app.models import CompaniesWaste
from app.client.schemes.Fkko import FkkoClientSchema
from app.client.schemes.Company import CompanyWasteSchema
from marshmallow import fields
from app.globals import db
import app.models as models
import json

class CompanyWasteClientSchema(ModelSchema):
    fkko = fields.Nested(FkkoClientSchema, only=("id", "name"))
    activity = fields.Method("getActivity")

    class Meta:
        model = CompaniesWaste

    def getActivity(self, el):
        if el.activity != None:
            return json.loads(el.activity)
        else:
            return None

class CompanyByWasteClientSchema(ModelSchema):
    company = fields.Method("getCompany")

    class Meta:
        model = CompaniesWaste

    def getActivity(self, el):
        if el.activity != None:
            return json.loads(el.activity)
        else:
            return None

    def getCompany(self, el):
        itn = el.itn
        company = db.session.query(models.Companies).filter(models.Companies.itn == itn).one_or_none()
        if company:
            schema = CompanyWasteSchema()
            return schema.dump(company)
        else:
            return None