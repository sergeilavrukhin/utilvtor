from app.models import Queries
from flask import Blueprint, jsonify
from app.client.schemes.Queries import QueriesClientSchema

app = Blueprint('ClientQueries', __name__)

@app.route("/")
def getQueries():
  queries = Queries.query.all()
  queriesSchema = QueriesClientSchema(many=True)
  return jsonify(queriesSchema.dump(queries)), 200
