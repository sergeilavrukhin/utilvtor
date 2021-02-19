from app.models import Region, Companies, CompaniesWaste
from flask import Blueprint, jsonify
from app.client.schemes.Company import CompanyClientSchema, CompanyClientShortSchema
from app.client.schemes.CompanyWaste import CompanyWasteClientSchema, CompanyByWasteClientSchema
from app.globals import db, POSTS_PER_PAGE
from flask_jwt_extended import jwt_optional, get_jwt_identity
import math

app = Blueprint('ClientCompanies', __name__)

@app.route("/<region>/")
@app.route("/<region>/page/<int:page>/")
def getCompaniesByRegion(region, page = 1):
  region = Region.query.filter_by(url = region).one_or_none()
  if region:
    dict = Companies.query.filter_by(region = region).paginate(page, POSTS_PER_PAGE, False).items
    dictSchema = CompanyClientSchema(many=True)
    c = db.session.query(Companies.id).filter_by(region = region).count()
    return jsonify({"companies": dictSchema.dump(dict), "name": region.text, "count": "{}".format(math.ceil(c/POSTS_PER_PAGE))}), 200
  else:
    return jsonify({"msg": "Регион не найден"}), 403

@app.route("/<int:c_id>/")
@jwt_optional
def getCompany(c_id):
  current_user = get_jwt_identity()
  dict = Companies.query.filter_by(id = c_id).one_or_none()
  if current_user:
    dictSchema = CompanyClientSchema()
  else:
    dictSchema = CompanyClientShortSchema()
  return jsonify(dictSchema.dump(dict)), 200

@app.route("/fkkolist/<int:c_id>/")
def getCompanyFkkoList(c_id):
  c = Companies.query.filter_by(id = c_id).one_or_none()

  if c:
    dict = CompaniesWaste.query.filter_by(itn = c.itn).all()
    dictSchema = CompanyWasteClientSchema(many=True)
    return jsonify(dictSchema.dump(dict)), 200
  else:
    return jsonify({"msg": "Компания не найдена"}), 403

@app.route("/byfkko/<int:code>/")
def getCompanyByFkko(code):
  dict = CompaniesWaste.query.with_entities(CompaniesWaste.itn).filter_by(fkko_id=code).group_by(CompaniesWaste.itn).limit(3)
  dictSchema = CompanyByWasteClientSchema(many=True)
  return jsonify(dictSchema.dump(dict)), 200