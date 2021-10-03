import validators
from models import Urls
from __init__ import db
from jsonschema import ValidationError
from flask_expects_json import expects_json
from schemas.schemas import urls_schema, url_schema
from utils.helpers import uid_generator
from flask import jsonify, Blueprint, make_response, request
from schemas.validation_shemas import get_short_link_schema, add_link_schema


api = Blueprint("api", __name__)


@api.errorhandler(400)
def bad_request(error):
    if isinstance(error.description, ValidationError):
        return make_response(jsonify({"error": error.description.message}), 400)
    return error


@api.route("/fetch_all", methods=["GET", "POST"])
def api_all():
    data = Urls.query.all()
    return make_response(jsonify(urls_schema.dump(data)), 200)


@api.route("/fetch_one", methods=["POST"])
@expects_json(get_short_link_schema)
def api_one():
    uid = request.json.get("uid", "")
    record = Urls.query.filter_by(uid=uid).first()
    if record is None:
        return make_response(jsonify({"error": "There are no results"}), 200)
    return make_response(jsonify(url_schema.dump(record)), 200)


@api.route("/add", methods=["POST"])
@expects_json(add_link_schema)
def add_link():
    long_link = request.json.get("link", "")
    days_left = int(request.json.get("expire_days", "")) if request.json.get("expire_days", "") else 90
    host_url = request.host_url

    # validate input fields
    if not validators.url(long_link) or days_left not in range(1, 365 + 1):
        return make_response(jsonify({"error": "you must provide a valid fields format!"}), 400)

    url_exist = Urls.query.filter_by(url=long_link).first()
    if url_exist is not None:
        url_uid = url_exist.uid
    else:
        url_uid = uid_generator()
        db.session.add(Urls(url=long_link, days_left=days_left, uid=url_uid, short_url=f"{host_url}{url_uid}"))
        db.session.commit()
    return make_response(jsonify({"short_url": f"{host_url}{url_uid}"}), 201)


