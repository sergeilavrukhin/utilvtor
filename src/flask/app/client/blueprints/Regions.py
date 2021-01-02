from app.models import Region
from flask import Blueprint, jsonify
from app.client.schemes.Region import RegionClientSchema

app = Blueprint('ClientRegions', __name__)

@app.route("/")
def getRegions():
  dict = Region.query.all()
  dictSchema = RegionClientSchema(many=True)
  return jsonify(dictSchema.dump(dict)), 200