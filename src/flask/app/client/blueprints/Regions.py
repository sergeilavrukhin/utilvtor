from app.models import Region
from flask import Blueprint, jsonify
from app.client.schemes.Region import RegionClientSchema

app = Blueprint('ClientRegions', __name__)

@app.route("/")
def getRegions():
  dict = Region.query.all()
  dictSchema = RegionClientSchema(many=True)
  return jsonify(dictSchema.dump(dict)), 200

@app.route("/list/")
def getRegionsList():
  dict = Region.query.all()
  dictSchema = RegionClientSchema(many=True, only=("id", "text"))
  return jsonify(dictSchema.dump(dict)), 200

@app.route("/list/all/")
def getRegionsListWithAll():
  dict = Region.query.all()
  data = {
    "id": 0,
    "text": "Все регионы"
  }
  dict.insert(0, data)
  dictSchema = RegionClientSchema(many=True, only=("id", "text"))
  return jsonify(dictSchema.dump(dict)), 200