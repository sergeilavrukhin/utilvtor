from app.models import Region, Companies
from flask import Blueprint, jsonify
from app.client.schemes.Company import CompanyClientSchema

app = Blueprint('ClientCompanies', __name__)

@app.route("/<region>/")
def getCompaniesByRegion(region):
  region = Region.query.filter_by(url = region).one_or_none()
  if region:
    print(region)
    dict = Companies.query.filter_by(region = region).limit(10)
    dictSchema = CompanyClientSchema(many=True)
    return jsonify(dictSchema.dump(dict)), 200
  else:
    return jsonify({"msg": "Регион не найден"}), 403

@app.route("/<int:c_id>/")
def getCompany(c_id):
  dict = Companies.query.filter_by(id = c_id).one_or_none()
  dictSchema = CompanyClientSchema()
  return jsonify(dictSchema.dump(dict)), 200