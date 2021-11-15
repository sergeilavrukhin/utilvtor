from ...models import Queries, User, QueryType, Region
from flask import Blueprint, request, jsonify, current_app
from ...functions import sendEmail, gen_password, mail_signup, mail_query_add
from ...globals import db, POSTS_PER_PAGE
from ...client.schemes.Queries import QueriesClientShortSchema, QueriesClientSchema, \
    QueryTypeClientSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
import math

app = Blueprint('ClientQueries', __name__)


@app.route("/")
@app.route("/page/<int:page>/")
def getQueries(page=1):
    dict = Queries.query.order_by(Queries.id.desc()).paginate(page, POSTS_PER_PAGE, False).items
    dictSchema = QueriesClientSchema(many=True)
    c = db.session.query(Queries.id).count()
    return jsonify(
        {"queries": dictSchema.dump(dict),
         "count": "{}".format(math.ceil(c / POSTS_PER_PAGE))}), 200


@app.route("/map")
def getMapList():
    list = Queries.query.all()
    mapSchema = QueriesClientSchema(many=True, only=("id",))
    return jsonify(mapSchema.dump(list)), 200


@app.route("/code/<int:id>")
def getQueriesByCode(id):
    queries = Queries.query.filter(Queries.fkko_id == id).all()
    queriesSchema = QueriesClientSchema(many=True)
    return jsonify(queriesSchema.dump(queries)), 200


@app.route("/<int:id>")
@jwt_required(optional=True)
def getQuery(id):
    queries = Queries.query.filter(Queries.id == id).one_or_none()
    queriesSchema = QueriesClientSchema()

    return jsonify(queriesSchema.dump(queries)), 200


@app.route("/", methods=["post"])
@jwt_required(optional=True)
def createQuery():
    password = gen_password()
    json = request.get_json()

    phone = json["phone"].replace('+', '').replace('(', '').replace(')', '').replace('-',
                                                                                     '').replace(
        ' ', '')
    if phone != "":
        user = User.query.filter(User.phone == phone).one_or_none()
        if user == None:
            user = User(json["firstname"], phone, json["email"], password,
                        current_app.config["SALT"])
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

# @app.route("/units/")
# def getUnits():
#  dict = Unit.query.all()
#  dictSchema = UnitClientSchema(many=True)
#  return jsonify(dictSchema.dump(dict)), 200
