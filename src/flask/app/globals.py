from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_redis import FlaskRedis

db = SQLAlchemy()
jwt = JWTManager()
redis = FlaskRedis()
POSTS_PER_PAGE = 10

activities = [
  "processing",
  "collection",
  "deactivation",
  "transportation",
  "utilization",
  "disposal",
]