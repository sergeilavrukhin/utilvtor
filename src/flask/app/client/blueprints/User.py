from app.models import User
from flask import Blueprint, request, jsonify, current_app
from app.globals import db
from app.functions import sendEmail, gen_password, mail_signup

app = Blueprint('ClientUser', __name__)

@app.route("/", methods=["post"])
def signUp():
  json = request.get_json()
  user = User.query.filter(User.email == json["email"]).one_or_none()
  if user:
    return jsonify({'msg': 'Пользователь с таким email уже зарегистрирован'}), 403
  else:
    phone = json["phone"].replace('+', '').replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
    password = gen_password()
    req = User(json["lastname"], json["firstname"], json["middlename"], "", phone, json["email"], json["itn"], password, current_app.config["SALT"])
    db.session.add(req)
    db.session.commit()
    mail_signup(json["email"], password)
    return jsonify({'msg': 'Пользователь успешно зарегистрирован. Информация для доступа отправлена вам на email.'}), 201