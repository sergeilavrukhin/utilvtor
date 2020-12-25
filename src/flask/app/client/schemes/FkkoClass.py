from marshmallow_sqlalchemy import ModelSchema
from app.models import FkkoClass

class FkkoClassClientSchema(ModelSchema):
    class Meta:
        model = FkkoClass