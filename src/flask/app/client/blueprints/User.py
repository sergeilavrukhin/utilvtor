from app.models import User
from flask import Blueprint, request, jsonify, current_app
from app.globals import db
from app.functions import sendEmail, gen_password, mail_signup
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, jwt_refresh_token_required, create_refresh_token

app = Blueprint('ClientUser', __name__)

@app.route("/sign-up/", methods=["POST"])
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

@app.route("/sign-in/", methods=["POST"])
def signIn():
  json = request.get_json()
  password = json["password"]
  user = User.query.filter(User.email == json["email"]).one_or_none()
  if user:
    if user.password == User.generateHash(password=password, salt=current_app.config["SALT"]):
      return jsonify({
        "access_token": create_access_token(identity=json["email"]),
        "refresh_token": create_refresh_token(identity=json["email"])
      }), 200

  return jsonify({'msg': 'Неверный логин или пароль'}), 403

@app.route('/refresh/', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    ret = {
        'access_token': create_access_token(identity=current_user)
    }
    return jsonify(ret), 200