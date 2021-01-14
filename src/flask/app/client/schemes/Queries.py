from marshmallow_sqlalchemy import ModelSchema
from app.models import Queries
from app.client.schemes.Fkko import FkkoClientSchema
from app.client.schemes.Unit import UnitClientSchema
from app.client.schemes.Aggr import AggrClientSchema
from app.client.schemes.QueryType import QueryTypeClientSchema
from app.client.schemes.Region import RegionClientSchema
from app.client.schemes.User import UserClientSchema
from marshmallow import fields


class QueriesClientSchema(ModelSchema):
    unit = fields.Nested(UnitClientSchema, only=("text",))
    aggr = fields.Nested(AggrClientSchema, only=("text",))
    query_type = fields.Nested(QueryTypeClientSchema, only=("text",))
    region = fields.Nested(RegionClientSchema, only=("text",))
    fkko = fields.Nested(FkkoClientSchema, only=("id",))
    user = fields.Nested(UserClientSchema, only=("id", "lastname", "middlename", "firstname", "email", "phone"))
    class Meta:
        model = Queries