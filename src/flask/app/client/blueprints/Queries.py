from app.models import Queries, User, Fkko, QueryType, Unit, Region
from flask import Blueprint, request, jsonify, current_app
from app.functions import sendEmail, gen_password, mail_signup, mail_query_add
from app.globals import db
from app.client.schemes.Queries import QueriesClientShortSchema, QueriesClientSchema, QueryTypeClientSchema
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
  #if current_user:
  #  queriesSchema = QueriesClientSchema()
  #else:
  #  queriesSchema = QueriesClientShortSchema()
  queriesSchema = QueriesClientSchema()

  return jsonify(queriesSchema.dump(queries)), 200

@app.route("/", methods=["post"])
@jwt_optional
def createQuery():
  current_user = get_jwt_identity()

  password = gen_password()
  json = request.get_json()
  phone = json["phone"].replace('+', '').replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
  if json["phone"] != "":
    user = User.query.filter(User.phone == json["phone"]).one_or_none()
    if user == None:
      user = User(json["firstname"], phone, password, current_app.config["SALT"])
      db.session.add(user)
  else:
    return jsonify({'msg': 'Не удалось разместить заявку'}), 403

  query_type = QueryType.query.filter(QueryType.id == json["query_type"]).one_or_none()
  region = Region.query.filter(Region.id == json["region"]).one_or_none()

  description = ""
  if json["description"] != "":
    description = json["description"]
  req = Queries(user, query_type, region, json["waste"], description)
  db.session.add(req)

  db.session.commit()

  mail_query_add(phone, json["waste"])
  return jsonify({'msg': 'Заявка успешно создана и отправлена на модерацию'}), 201

@app.route("/query_types/")
def getQueryTypes():
  dict = QueryType.query.all()
  dictSchema = QueryTypeClientSchema(many=True)
  return jsonify(dictSchema.dump(dict)), 200

#@app.route("/units/")
#def getUnits():
#  dict = Unit.query.all()
#  dictSchema = UnitClientSchema(many=True)
#  return jsonify(dictSchema.dump(dict)), 200