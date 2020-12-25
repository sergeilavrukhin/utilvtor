from marshmallow_sqlalchemy import ModelSchema
from app.models import Aggregation

class AggrClientSchema(ModelSchema):
    class Meta:
        model = Aggregation