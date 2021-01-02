from app.models import Queries, User, Fkko, QueryType, Unit, Region
from flask import Blueprint, request, jsonify, current_app
from app.functions import sendEmail, gen_password, mail_signup, mail_query_add
from app.globals import db
from app.client.schemes.Queries import QueriesClientSchema, QueryTypeClientSchema, UnitClientSchema

app = Blueprint('ClientQueries', __name__)

@app.route("/")
def getQueries():
  queries = Queries.query.all()
  queriesSchema = QueriesClientSchema(many=True)
  return jsonify(queriesSchema.dump(queries)), 200

@app.route("/<int:id>")
def getQuery(id):
  queries = Queries.query.filter(Queries.id == id).one_or_none()
  queriesSchema = QueriesClientSchema()
  return jsonify(queriesSchema.dump(queries)), 200

@app.route("/", methods=["post"])
def createQuery():
  json = request.get_json()
  user = User.query.filter(User.email == json["email"]).one_or_none()
  if user:
    return jsonify({'msg': 'Пользователь с таким email уже зарегистрирован'}), 403
  else:
    phone = json["phone"].replace('+', '').replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
    password = gen_password()
    user = User(json["lastname"], json["firstname"], json["middlename"], "", phone, json["email"], json["itn"], password, current_app.config["SALT"])
    db.session.add(user)

    fkko = None
    if json["fkko"].isdigit():
      fkko = Fkko.query.filter(Fkko.id == int(json["fkko"])).one_or_none()
    if fkko:
      aggr = fkko.aggr
      waste = fkko.name
    else:
      aggr = None
      waste = json["fkko"]
    print(json["query_type"])
    query_type = QueryType.query.filter(QueryType.id == json["query_type"]).one_or_none()
    unit = Unit.query.filter(Unit.id == json["bu"]).one_or_none()
    region = Region.query.filter(Region.id == json["region"]).one_or_none()

    req = Queries(fkko, unit, aggr, user, query_type, region, waste, json["count"], json["address"], 0)
    db.session.add(req)

    db.session.commit()
    mail_signup(json["email"], password)
    mail_query_add()
    return jsonify({'msg': 'Заявка успешно создана и отправлена на модерацию'}), 201

@app.route("/query_types/")
def getQueryTypes():
  dict = QueryType.query.all()
  dictSchema = QueryTypeClientSchema(many=True)
  return jsonify(dictSchema.dump(dict)), 200

@app.route("/units/")
def getUnits():
  dict = Unit.query.all()
  dictSchema = UnitClientSchema(many=True)
  return jsonify(dictSchema.dump(dict)), 200