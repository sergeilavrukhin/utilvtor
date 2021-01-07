from app.models import User
from flask import Blueprint, request, jsonify, current_app
from app.globals import db
from app.functions import sendEmail, gen_password, mail_signup, mail_recovery
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


@app.route("/recovery/", methods=["POST"])
def recovery():
  json = request.get_json()
  user = User.query.filter(User.email == json["email"]).one_or_none()
  if user:
    password = gen_password()
    user.setPassword(password, current_app.config["SALT"])
    db.session.commit()
    mail_recovery(json["email"], password)
    return jsonify({'msg': 'Новый пароль отправлен вам на email'}), 200

  return jsonify({'msg': 'Неверный логин или пароль'}), 403

@app.route('/refresh/', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    ret = {
        'access_token': create_access_token(identity=current_user)
    }
    return jsonify(ret), 200

@app.route('/')
@jwt_required
def user():
    current_user = get_jwt_identity()
    user = User.query.filter(User.email == current_user).one_or_none()
    ret = {
        'user': current_user,
        'email': user.email,
        'firstname': user.firstname,
        'middlename': user.middlename,
        'lastname': user.lastname,
        'phone': user.phone,
        'itn': user.itn
    }
    return jsonify(ret), 200

@app.route("/edit/", methods=["POST"])
@jwt_required
def edit():
  current_user = get_jwt_identity()
  json = request.get_json()
  user = User.query.filter(User.email == current_user).one_or_none()
  if user:
    if "firstname" in json:
      user.setFirstname(json["firstname"])

    if "middlename" in json:
      user.setMiddlename(json["middlename"])

    if "lastname" in json:
      user.setLastname(json["lastname"])

    if "phone" in json:
      phone = json["phone"].replace('+', '').replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
      user.setPhone(phone)

    if "itn" in json:
      user.setITN(json["itn"])

    db.session.commit()
    return jsonify({'msg': 'Данные пользователя успешно изменены'}), 200

@app.route('/logout/', methods=["POST"])
@jwt_required
def logout():
    current_user = get_jwt_identity()
    ret = {
        'user': current_user
    }
    return jsonify(ret), 200