from app.models import User
from flask import Blueprint, request, jsonify, current_app, render_template
from app.globals import db
from app.functions import sendEmail
import random

app = Blueprint('ClientUser', __name__)

@app.route("/", methods=["post"])
def signUp():
  json = request.get_json()
  user = User.query.filter(User.email == json["email"]).all()
  if user:
    return jsonify({'msg': 'Пользователь с таким email уже зарегистрирован'}), 403
  else:
    password = ''
    for x in range(10):  # Количество символов (16)
      password = password + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))

    req = User(json["lastname"], json["firstname"], json["middlename"], "", json["phone"], json["email"], json["itn"], password, current_app.config["SALT"])
    db.session.add(req)
    db.session.commit()

    subject = "Добро пожаловать на сайт Веботход.ру"
    html = render_template("mail_signup.tpl",
      title=subject,
      login=json["email"],
      password=password)

    sendEmail.delay(json["email"], subject, html)
    return jsonify({'msg': 'Пользователь успешно зарегистрирован'}), 201