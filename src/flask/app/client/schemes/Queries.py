from marshmallow_sqlalchemy import ModelSchema
from app.models import QueryModel


class QueriesClientSchema(ModelSchema):
    class Meta:
        model = QueryModel