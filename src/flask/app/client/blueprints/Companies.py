from app.models import Region, Companies, CompaniesWaste, Fkko, SiteClick
from flask import Blueprint, jsonify
from app.client.schemes.Company import CompanyClientSchema
from app.client.schemes.CompanyWaste import CompanyWasteClientSchema
from app.client.schemes.Region import RegionClientSchema
from app.client.schemes.Fkko import FkkoClientSchema
from app.globals import db, POSTS_PER_PAGE, activities
from sqlalchemy import or_, and_
import math
import json

app = Blueprint('ClientCompanies', __name__)

@app.route("/map")
def getMapList():
  list = Companies.query.all()
  mapSchema = CompanyClientSchema(many=True, only=("id",))
  return jsonify(mapSchema.dump(list)), 200

@app.route("/region/map")
def getRegionMapList():
  list = Region.query.all()
  mapSchema = RegionClientSchema(many=True, only=("url",))
  return jsonify(mapSchema.dump(list)), 200

@app.route("/region/activity/map")
def getRegionActivityMapList():
  list = Region.query.all()
  region_activity = []
  for region in list:
    for activity in activities:
      data = {"url": region.url, "activity": activity}
      region_activity.append(data)
  return jsonify(region_activity), 200

@app.route("/search/map")
def getSearchMapList():
  list = Fkko.query.all()
  mapSchema = FkkoClientSchema(many=True, only=("id",))
  return jsonify(mapSchema.dump(list)), 200

@app.route("/<region>/")
@app.route("/<region>/page/<int:page>/")
@app.route("/<region>/activity/<activity>/")
@app.route("/<region>/activity/<activity>/page/<int:page>/")
def getCompaniesByRegion(region, page = 1, activity = None):
  region = Region.query.filter_by(url = region).one_or_none()
  if region:
    if activity:
      activitysearch = "%{}%".format(activity)
      dict = Companies.query.filter(Companies.activity.like(activitysearch), Companies.region==region).paginate(page, POSTS_PER_PAGE, False).items
      dictSchema = CompanyClientSchema(many=True)
      c = db.session.query(Companies.id).filter(Companies.activity.like(activitysearch), Companies.region==region).count()
    else:
      dict = Companies.query.filter_by(region = region).paginate(page, POSTS_PER_PAGE, False).items
      dictSchema = CompanyClientSchema(many=True)
      c = db.session.query(Companies.id).filter_by(region = region).count()
    return jsonify({"companies": dictSchema.dump(dict), "name": region.text, "count": "{}".format(math.ceil(c/POSTS_PER_PAGE))}), 200
  else:
    return jsonify({"msg": "Регион не найден"}), 403

@app.route("/search/<search>/")
@app.route("/search/<search>/region/<region>/")
@app.route("/search/<search>/page/<int:page>/")
@app.route("/search/<search>/activity/<activity>/")
@app.route("/search/<search>/activity/<activity>/page/<int:page>/")
@app.route("/search/<search>/region/<region>/page/<int:page>/")
@app.route("/search/<search>/region/<region>/activity/<activity>/")
@app.route("/search/<search>/region/<region>/activity/<activity>/page/<int:page>/")
def getSearchCompanies(search, region = 0, page = 1, activity = None):
  likesearch = "%{}%".format(search)

  in_company = []
  cw =  db.session.query(CompaniesWaste.itn).with_entities(CompaniesWaste.itn).filter_by(fkko_id=search.replace(' ', '')).group_by(
    CompaniesWaste.itn).all()
  for row in cw:
    in_company.append(row.itn)

  fkkolist = []
  cwn = db.session.query(Fkko.id).filter(Fkko.name.like(likesearch)).limit(1000)
  for row in cwn:
    fkkolist.append(row.id)

  if len(fkkolist) > 0:
    cw = db.session.query(CompaniesWaste.itn).with_entities(CompaniesWaste.itn).filter(CompaniesWaste.fkko_id.in_(fkkolist)).group_by(
      CompaniesWaste.itn).all()
    for row in cw:
      in_company.append(row.itn)

  if region == 0:
    if activity:
      activitysearch = "%{}%".format(activity)
      c = db.session.query(Companies.id).filter(or_(and_(Companies.activity.like(activitysearch), Companies.name.like(likesearch)),and_(Companies.activity.like(activitysearch), Companies.itn.in_(in_company)))).count()
      dict = Companies.query.filter(or_(and_(Companies.activity.like(activitysearch), Companies.name.like(likesearch)), and_(Companies.activity.like(activitysearch), Companies.itn.in_(in_company)))).paginate(page, POSTS_PER_PAGE, False).items
    else:
      c = db.session.query(Companies.id).filter(or_(Companies.name.like(likesearch), Companies.itn.in_(in_company))).count()
      dict = Companies.query.filter(or_(Companies.name.like(likesearch), Companies.itn.in_(in_company))).paginate(page, POSTS_PER_PAGE, False).items
  else:
    if activity:
      activitysearch = "%{}%".format(activity)
      c = db.session.query(Companies.id).filter(and_(Companies.activity.like(activitysearch), or_(Companies.name.like(likesearch), Companies.itn.in_(in_company)),Companies.region_id == region)).count()
      dict = Companies.query.filter(and_(Companies.activity.like(activitysearch), or_(Companies.name.like(likesearch), Companies.itn.in_(in_company)), Companies.region_id == region)).paginate(page, POSTS_PER_PAGE, False).items
    else:
      c = db.session.query(Companies.id).filter(and_(or_(Companies.name.like(likesearch), Companies.itn.in_(in_company)), Companies.region_id == region)).count()
      dict = Companies.query.filter(and_(or_(Companies.name.like(likesearch), Companies.itn.in_(in_company)), Companies.region_id == region)).paginate(page, POSTS_PER_PAGE, False).items

  dictSchema = CompanyClientSchema(many=True)
  return jsonify({"companies": dictSchema.dump(dict), "count": "{}".format(math.ceil(c/POSTS_PER_PAGE))}), 200

@app.route("/<int:c_id>/")
def getCompany(c_id):
  dict = Companies.query.filter_by(id = c_id).one_or_none()
  dictSchema = CompanyClientSchema()
  return jsonify(dictSchema.dump(dict)), 200

@app.route("/siteclick/<int:c_id>/")
def CompanySiteClick(c_id):
  company = Companies.query.filter_by(id = c_id).one_or_none()
  siteclick = SiteClick(company)
  db.session.add(siteclick)
  db.session.commit()
  return jsonify({"msg": "ok"}), 201

@app.route("/<int:c_id>/contacts/<type>/")
def getCompanyContacts(c_id, type):
  company = Companies.query.filter_by(id = c_id).one_or_none()
  data = 'get'
  if type == 'locality':
    if company.locality != None:
      data = company.locality

  if type == 'site':
    if company.site != None:
      try:
        data = json.loads(company.site)
      except:
        data = json.loads("[\"{}\"]".format(company.site))

  if type == 'emails':
    if company.emails != None:
      data = json.loads(company.emails)

  if type == 'phones':
    if company.phones != None:
      data = json.loads(company.phones)

  return jsonify({'data': data}), 200

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
  in_company = []
  cw = CompaniesWaste.query.with_entities(CompaniesWaste.itn).filter_by(fkko_id=code).group_by(
    CompaniesWaste.itn).all()

  for row in cw:
    in_company.append(row.itn)

  dict = Companies.query.filter(Companies.itn.in_(in_company)).limit(3)

  dictSchema = CompanyClientSchema(many=True)
  return jsonify(dictSchema.dump(dict)), 200