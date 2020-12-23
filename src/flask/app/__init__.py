from flask import Flask
from flask_migrate import Migrate
from .globals import db, jwt
from .models import *

def create_backend_app():
  app = Flask(__name__)
  app.config.from_pyfile("config.production.py")
  db.init_app(app)
  Migrate(app, db)
  jwt.init_app(app)


  from .client.blueprints.Queries import app as Queries
  from .client.blueprints.Fkko import app as Fkko
  from .client.blueprints.User import app as User
  root_client_api = "/api/client/"
  app.register_blueprint(Queries, url_prefix=root_client_api + "queries")
  app.register_blueprint(Fkko, url_prefix=root_client_api + "code")
  app.register_blueprint(User, url_prefix=root_client_api + "signup")


  return app

backend_app = create_backend_app()