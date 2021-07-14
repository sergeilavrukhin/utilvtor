from marshmallow_sqlalchemy import ModelSchema
from app.models import Queries
from app.client.schemes.QueryType import QueryTypeClientSchema
from app.client.schemes.Region import RegionClientSchema
from app.client.schemes.User import UserClientSchema
from marshmallow import fields


class QueriesClientSchema(ModelSchema):
    query_type = fields.Nested(QueryTypeClientSchema, only=("text",))
    region = fields.Nested(RegionClientSchema, only=("text",))
    user = fields.Nested(UserClientSchema, only=("id", "firstname", "phone", "email"))
    date_create = fields.Method("getDate")
    class Meta:
        model = Queries

    def getDate(self, el):
        return el.date_create.strftime("%d.%m.%Y")

class QueriesClientShortSchema(ModelSchema):
    query_type = fields.Nested(QueryTypeClientSchema, only=("text",))
    region = fields.Nested(RegionClientSchema, only=("text",))
    user = fields.Method("getUser")
    class Meta:
        model = Queries

    def getUser(self, el):
        return None