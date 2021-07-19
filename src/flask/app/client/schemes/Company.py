from marshmallow_sqlalchemy import ModelSchema
from app.models import Companies
from app.client.schemes.Region import RegionClientSchema
from marshmallow import fields
import json

class CompanyClientSchema(ModelSchema):
    value = fields.Method("getValue")
    activity = fields.Method("getActivity")
    gps = fields.Method("getGPS")
    region = fields.Nested(RegionClientSchema, only=('text', 'url'))
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
            try:
                data = json.loads(el.activity)
            except:
                data = None
            return data
        else:
            return None

    def getGPS(self, el):
        if el.gps != None:
            try:
                data = json.loads(el.gps)
            except:
                data = None
            return data
        else:
            return None

    def getPhones(self, el):
        if el.phones != None:
            try:
                data = json.loads(el.phones)
            except:
                data = None
            return data
        else:
            return None

    def getEmails(self, el):
        if el.emails != None:
            try:
                data = json.loads(el.emails)
            except:
                data = None
            return data
        else:
            return None

    def getSite(self, el):
        if el.site != None:
            try:
                data = json.loads(el.site)
            except:
                try:
                    data = json.loads("[\"{}\"]".format(el.site))
                except:
                    data = None
            return data
        else:
            return None

    def getLocality(self, el):
        if el.locality != None:
            return el.locality
        else:
            return None


class CompanyWasteSchema(ModelSchema):
    gps = fields.Method("getGPS")
    activity = fields.Method("getActivity")

    class Meta:
        model = Companies

    def getGPS(self, el):
        if el.gps:
            return json.loads(el.gps)
        else:
            return None

    def getActivity(self, el):
        if el.activity != None:
            return json.loads(el.activity)
        else:
            return None