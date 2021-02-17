from marshmallow_sqlalchemy import ModelSchema
from app.models import Companies
from marshmallow import fields
import json

class CompanyClientSchema(ModelSchema):
    value = fields.Method("getValue")
    activity = fields.Method("getActivity")
    gps = fields.Method("getGPS")
    emails = fields.Method("getEmails")
    phones = fields.Method("getPhones")

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

    def getPhones(self, el):
        if el.phones != None:
            return json.loads(el.phones)
        else:
            return None

    def getEmails(self, el):
        if el.emails != None:
            return json.loads(el.emails)
        else:
            return None

class CompanyClientShortSchema(ModelSchema):
    value = fields.Method("getValue")
    activity = fields.Method("getActivity")
    gps = fields.Method("getGPS")
    emails = fields.Method("getEmails")
    phones = fields.Method("getPhones")
    site = fields.Method("getSite")
    locality = fields.Method("getLocality")

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

    def getPhones(self, el):
        if el.phones != None:
            return "reg"
        else:
            return None

    def getEmails(self, el):
        if el.emails != None:
            return "reg"
        else:
            return None

    def getSite(self, el):
        if el.site != None:
            return "reg"
        else:
            return None

    def getLocality(self, el):
        if el.locality != None:
            return "reg"
        else:
            return None