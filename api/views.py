from flask import Blueprint, jsonify
from flask_cors import cross_origin
from flask_restful import Api
from marshmallow import ValidationError

from api.resources.user import UserList, UserResource

blueprint = Blueprint("api", __name__, url_prefix="/api")
api = Api(blueprint, errors=blueprint.errorhandler)

api.add_resource(UserList, "/users")
api.add_resource(UserResource, "/users/<int:user_id>")


@blueprint.route("/test-cors")
@cross_origin()
def test_cors():
    return {}


@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    return jsonify(e.messages), 400
