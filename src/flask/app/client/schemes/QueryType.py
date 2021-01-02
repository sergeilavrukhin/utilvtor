from marshmallow_sqlalchemy import ModelSchema
from app.models import QueryType
from marshmallow import fields

class QueryTypeClientSchema(ModelSchema):
    value = fields.Method("getValue")
    class Meta:
        model = QueryType

    def getValue(self, el):
        return el.id