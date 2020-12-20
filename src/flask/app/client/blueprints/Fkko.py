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
  title = "Блоки кодов ФККО"
  subtitle = "Классификация осуществляется по нескольким признакам, оцениваемым в совокупности: происхождению, агрегатному состоянию, степени вредного воздействия и опасным свойствам."
  return jsonify({"title": title, "subtitle": subtitle, "codes": codesSchema.dump(codes)}), 200

@app.route("/<int:fkko_id>")
def getFkkoById(fkko_id):
  codes = Fkko.query.filter(Fkko.parent_id == fkko_id).all()
  codesSchema = FkkoClientSchema(many=True, only=("id", "name"))
  fkko = Fkko.query.filter(Fkko.id == fkko_id).one_or_none()
  fkkoclass = FkkoClass.query.filter(FkkoClass.id == fkko.fkkoclass_id).one_or_none()
  fkkoclassSchema = FkkoClassClientSchema()
  parents.clear()
  fkkoparents = getParents(fkko.parent_id)
  fkkoparents.reverse()
  aggrname = ""
  aggr = Aggregation.query.filter(Aggregation.id == fkko.aggr_id).one_or_none()
  if aggr:
    aggrname = aggr.name
  return jsonify({"title": fkko.name, "subtitle": "", "parents": fkkoparents, "aggrname": aggrname, "fkkoclass": fkkoclassSchema.dump(fkkoclass), "codes": codesSchema.dump(codes)}), 200
