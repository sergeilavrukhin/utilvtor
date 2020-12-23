from app.models import User
from flask import Blueprint, request, jsonify, current_app
from app.client.schemes.User import UserClientSchema
from app.globals import db

app = Blueprint('ClientUser', __name__)

parents = []

@app.route("/", methods=["post"])
def signUp():
  json = request.get_json()
  user = User.query.filter(User.email == json["email"]).all()
  if user:
    return jsonify({'msg': 'Пользователь с таким email уже зарегистрирован'}), 403
  else:

    req = User(json["lastname"], json["firstname"], json["middlename"], "", json["phone"], json["email"], json["password"], current_app.config["SALT"])
    db.session.add(req)
    db.session.commit()
    return jsonify({'msg': 'Пользователь успешно зарегистрирован'}), 201