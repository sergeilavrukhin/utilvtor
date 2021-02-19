from app.models import Queries, User, Fkko, QueryType, Unit, Region
from flask import Blueprint, request, jsonify, current_app
from app.functions import sendEmail, gen_password, mail_signup, mail_query_add
from app.globals import db
from app.client.schemes.Queries import QueriesClientShortSchema, QueriesClientSchema, QueryTypeClientSchema, UnitClientSchema
from flask_jwt_extended import jwt_optional, jwt_required, get_jwt_identity

app = Blueprint('ClientQueries', __name__)

@app.route("/")
def getQueries():
  queries = Queries.query.order_by(Queries.id.desc()).all()
  queriesSchema = QueriesClientSchema(many=True)
  return jsonify(queriesSchema.dump(queries)), 200


@app.route("/map")
def getQueryList():
  queries = Queries.query.all()
  queriesSchema = QueriesClientSchema(many=True, only=("id",))
  return jsonify(queriesSchema.dump(queries)), 200

@app.route("/code/<int:id>")
def getQueriesByCode(id):
  queries = Queries.query.filter(Queries.fkko_id == id).all()
  queriesSchema = QueriesClientSchema(many=True)
  return jsonify(queriesSchema.dump(queries)), 200

@app.route("/<int:id>")
@jwt_optional
def getQuery(id):
  current_user = get_jwt_identity()
  queries = Queries.query.filter(Queries.id == id).one_or_none()
  if current_user:
    queriesSchema = QueriesClientSchema()
  else:
    queriesSchema = QueriesClientShortSchema()
  return jsonify(queriesSchema.dump(queries)), 200

@app.route("/", methods=["post"])
@jwt_optional
def createQuery():
  current_user = get_jwt_identity()

  password = gen_password()
  json = request.get_json()
  if json["email"] != "":
    user = User.query.filter(User.email == json["email"]).one_or_none()
    if user:
      return jsonify({'msg': 'Пользователь с таким email уже зарегистрирован'}), 403
    else:
      phone = json["phone"].replace('+', '').replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
      user = User(json["lastname"], json["firstname"], json["middlename"], "", phone, json["email"], json["itn"],
                  password, current_app.config["SALT"])
      db.session.add(user)
  else:
    user = User.query.filter(User.email == current_user).one_or_none()

  fkko = None
  if isinstance(json["fkko"], int):
    fkko = Fkko.query.filter(Fkko.id == int(json["fkko"])).one_or_none()

  if fkko:
    aggr = fkko.aggr
  else:
    aggr = None

  query_type = QueryType.query.filter(QueryType.id == json["query_type"]).one_or_none()
  unit = Unit.query.filter(Unit.id == json["bu"]).one_or_none()
  region = Region.query.filter(Region.id == json["region"]).one_or_none()

  req = Queries(fkko, unit, aggr, user, query_type, region, json["waste"], json["count"], json["address"], 0)
  db.session.add(req)

  db.session.commit()
  if json["email"] != "":
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