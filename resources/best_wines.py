from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required, fresh_jwt_required

REPORT_NOT_FOUND = "The report with uuid {} does not exist"
MALFORMED_REQUEST = "Malformed request"

class BestWines(Resource):


