from app.models import User
from flask import Blueprint, request, jsonify, current_app
from app.globals import db
from app.functions import sendEmail

app = Blueprint('ClientUser', __name__)

@app.route("/", methods=["post"])
def signUp():
  json = request.get_json()
  user = User.query.filter(User.email == json["email"]).all()
  if user:
    return jsonify({'msg': 'Пользователь с таким email уже зарегистрирован'}), 403
  else:
    req = User(json["lastname"], json["firstname"], json["middlename"], "", json["phone"], json["email"], json["itn"], "password", current_app.config["SALT"])
    db.session.add(req)
    db.session.commit()
    sendEmail.delay(json["email"], "Добро пожаловать на сайт Веботход.ру", "Пользователь успешно зарегистрирован")
    return jsonify({'msg': 'Пользователь успешно зарегистрирован'}), 201