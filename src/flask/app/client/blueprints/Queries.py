from app.models import QueryModel
from flask import Blueprint, jsonify
from app.client.schemes.Queries import QueriesClientSchema

app = Blueprint('ClientQueries', __name__)

@app.route("/")
def getQueries():
  queries = QueryModel.query.all()
  queriesSchema = QueriesClientSchema(many=True)
  return jsonify(queriesSchema.dump(queries)), 200
