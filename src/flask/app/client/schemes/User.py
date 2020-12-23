from marshmallow_sqlalchemy import ModelSchema
from app.models import User

class UserClientSchema(ModelSchema):
    class Meta:
        model = User