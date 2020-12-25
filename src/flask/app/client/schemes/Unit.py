from marshmallow_sqlalchemy import ModelSchema
from app.models import Unit

class UnitClientSchema(ModelSchema):
    class Meta:
        model = Unit