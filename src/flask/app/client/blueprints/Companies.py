from app.models import Region, Companies
from flask import Blueprint, jsonify
from app.client.schemes.Company import CompanyClientSchema
from app.globals import db, POSTS_PER_PAGE
import math

app = Blueprint('ClientCompanies', __name__)

@app.route("/<region>/")
@app.route("/<region>/page/<int:page>/")
def getCompaniesByRegion(region, page = 1):
  region = Region.query.filter_by(url = region).one_or_none()
  if region:
    dict = Companies.query.filter_by(region = region).paginate(page, POSTS_PER_PAGE, False).items
    dictSchema = CompanyClientSchema(many=True)
    return jsonify(dictSchema.dump(dict)), 200
  else:
    return jsonify({"msg": "Регион не найден"}), 403

@app.route("/<region>/count/")
def getCompaniesByRegionCount(region):
  region = Region.query.filter_by(url = region).one_or_none()
  if region:
    c = db.session.query(Companies.id).filter_by(region = region).count()
    return "{}".format(math.ceil(c/POSTS_PER_PAGE))
  else:
    return 0

@app.route("/<int:c_id>/")
def getCompany(c_id):
  dict = Companies.query.filter_by(id = c_id).one_or_none()
  dictSchema = CompanyClientSchema()
  return jsonify(dictSchema.dump(dict)), 200