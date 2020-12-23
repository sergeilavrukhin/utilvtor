from marshmallow_sqlalchemy import ModelSchema
from app.models import Queries, Unit, QueryType, Aggregation
from app.client.schemes.Fkko import FkkoClientSchema
from marshmallow import fields

class UnitClientSchema(ModelSchema):
    class Meta:
        model = Unit

class AggrClientSchema(ModelSchema):
    class Meta:
        model = Aggregation

class QueryTypeClientSchema(ModelSchema):
    class Meta:
        model = QueryType

class QueriesClientSchema(ModelSchema):
    unit = fields.Nested("UnitClientSchema", only=("name",))
    aggr = fields.Nested("AggrClientSchema", only=("name",))
    query_type = fields.Nested("QueryTypeClientSchema", only=("name",))
    fkko = fields.Nested("FkkoClientSchema", only=("id",))
    class Meta:
        model = Queries