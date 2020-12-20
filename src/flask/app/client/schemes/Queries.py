from marshmallow_sqlalchemy import ModelSchema
from app.models import Queries


class QueriesClientSchema(ModelSchema):
    class Meta:
        model = Queries