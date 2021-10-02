import requests
from models import Urls
from __init__ import app, db
from utils.helpers import url_expired
from api.api import api as api_blueprint
from flask import render_template, request, redirect, make_response, flash, url_for


app.register_blueprint(api_blueprint, url_prefix="/api/v1")


@app.errorhandler(404)
def not_found(error):
    return make_response(render_template("404.html", body="dark"), 404)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        response = requests.post(f"{request.host_url}/api/v1/add", json={
            "link": request.form.get("long-url"),
            "expire_days": int(request.form.get("days_left"))
        }, timeout=60)
        short_url = response.json().get("short_url")
        flash("Your link converted", category='success')
        return make_response(render_template("index.html", short_url=short_url), 201)

    return make_response(render_template("index.html"), 200)


@app.route("/<url_uid>")
def url_redirect(url_uid):
    url = Urls.query.filter_by(uid=url_uid).first()
    if url is not None:
        if not url_expired(url.expire_at):
            return redirect(url.url, code=301)
        db.session.delete(url)
        db.session.commit()
        flash("Link is expired!", category="danger")
        return redirect(url_for('index'))
    flash("Incorrect link id!", category="danger")
    return redirect(url_for('index'))


@app.route("/all_info")
def all_info():
    response = requests.get(f"{request.host_url}/api/v1/fetch_all", timeout=60)
    data = response.json()
    if data:
        return make_response(render_template("info.html", data=data, table_style="table"), 200)
    flash("There is no links data", category='danger')
    return make_response(render_template("info.html"), 200)


@app.route("/get_url", methods=["POST", "GET"])
def get_url_by_id():
    if request.method == "POST":
        response = requests.post(f"{request.host_url}api/v1/fetch_one", json={
            "uid": request.form.get("uid").strip()
        })
        if response.json().get("error", ""):
            flash("There is no link for the given id or id is incorrect!", category="danger")
            return redirect(url_for('index'))
        flash("Found url!", category="success")
        return make_response(render_template("get.url.html", link=response.json().get("url")), 200)
    return make_response(render_template("get.url.html"), 200)


if __name__ == '__main__':
    app.run()
