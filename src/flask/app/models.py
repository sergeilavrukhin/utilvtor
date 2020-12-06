from .globals import db

class QueryModel(db.Model):
  __tablename__ = "queries"
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer)