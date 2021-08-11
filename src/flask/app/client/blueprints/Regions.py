from app.models import Region
from flask import Blueprint, jsonify
from app.client.schemes.Region import RegionClientSchema
from pysyge import GeoLocator
import os

app = Blueprint('ClientRegions', __name__)

@app.route("/")
def getRegions():
  dict = Region.query.all()
  dictSchema = RegionClientSchema(many=True)
  return jsonify(dictSchema.dump(dict)), 200

@app.route("/list/")
def getRegionsList():
  dict = Region.query.all()
  dictSchema = RegionClientSchema(many=True, only=("value", "text"))
  return jsonify(dictSchema.dump(dict)), 200

@app.route("/list/all/")
def getRegionsListWithAll():
  dict = Region.query.all()
  data = {
    "id": 0,
    "value": 0,
    "text": "Все регионы"
  }
  dict.insert(0, data)
  dictSchema = RegionClientSchema(many=True, only=("value", "text"))
  return jsonify(dictSchema.dump(dict)), 200

@app.route("/define/<ip>/")
def defineRegionByIp(ip):
  geodata = GeoLocator('datafiles/SxGeoCity.dat')

  location = geodata.get_location(ip, detailed=True)

  if "info" in location:
    return jsonify({"msg": location['info']['region']['iso']})
  else:
    return jsonify({"msg": "not found"})