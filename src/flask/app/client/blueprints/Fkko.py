from app.models import Fkko, FkkoClass, Aggregation
from flask import Blueprint, jsonify
from app.client.schemes.Fkko import FkkoClientSchema, FkkoClassClientSchema

app = Blueprint('ClientFkko', __name__)

parents = []

def getParents(parent_id):
  fkko = Fkko.query.filter(Fkko.id == parent_id).one_or_none()
  if fkko:
    parent = {
      "id": fkko.id,
      "name": fkko.name,
    }
    parents.append(parent)
    getParents(fkko.parent_id)
  return parents

@app.route("/")
def getFkko():
  codes = Fkko.query.filter(Fkko.parent_id == None).all()
  codesSchema = FkkoClientSchema(many=True, only=("id", "name"))
  return jsonify(codesSchema.dump(codes)), 200

@app.route("/map")
def getFkkoList():
  codes = Fkko.query.all()
  codesSchema = FkkoClientSchema(many=True, only=("id",))
  return jsonify(codesSchema.dump(codes)), 200

@app.route("/<int:fkko_id>")
def getFkkoById(fkko_id):
  codes = Fkko.query.filter(Fkko.parent_id == fkko_id).all()
  codesSchema = FkkoClientSchema(many=True, only=("id", "name"))
  fkko = Fkko.query.filter(Fkko.id == fkko_id).one_or_none()
  fkkoSchema = FkkoClientSchema()

  parents.clear()
  breadcrumb = getParents(fkko.parent_id)
  breadcrumb.reverse()
  return jsonify({"breadcrumb": breadcrumb, "fkko": fkkoSchema.dump(fkko), "codes": codesSchema.dump(codes)}), 200
