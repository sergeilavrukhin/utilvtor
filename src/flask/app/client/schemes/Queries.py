from marshmallow_sqlalchemy import ModelSchema
from app.models import Queries
from app.client.schemes.Fkko import FkkoClientSchema
from app.client.schemes.Unit import UnitClientSchema
from app.client.schemes.Aggr import AggrClientSchema
from app.client.schemes.QueryType import QueryTypeClientSchema
from marshmallow import fields


class QueriesClientSchema(ModelSchema):
    unit = fields.Nested(UnitClientSchema, only=("name",))
    aggr = fields.Nested(AggrClientSchema, only=("name",))
    query_type = fields.Nested(QueryTypeClientSchema, only=("name",))
    fkko = fields.Nested(FkkoClientSchema, only=("id",))
    class Meta:
        model = Queries