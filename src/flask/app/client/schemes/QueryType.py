from marshmallow_sqlalchemy import ModelSchema
from app.models import QueryType

class QueryTypeClientSchema(ModelSchema):
    class Meta:
        model = QueryType