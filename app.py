import uuid
from models import Urls
from __init__ import app, db
from flask import render_template, request, redirect, make_response, flash, url_for


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        long_url = request.form.get("long-url")
        url_exist = Urls.query.filter_by(url=long_url).first()
        if url_exist:
            url_uid = url_exist.uid
        else:
            url_uid = str(uuid.uuid4())[:10]
            db.session.add(Urls(url=long_url, uid=url_uid))
            db.session.commit()

        short_url = f"{request.host_url}short/{url_uid}"
        flash("Your link converted", category='success')
        return make_response(render_template("index.html", short_url=short_url), 201)

    return make_response(render_template("index.html"), 200)


@app.route("/short/<url_uid>")
def url_redirect(url_uid):
    url = Urls.query.filter_by(uid=url_uid).first()
    if not url:
        flash("Incorrect url id!", category="danger")
        return redirect(url_for('index'))
    return redirect(url.url, code=301)


@app.route("/all_info")
def all_info():
    data = Urls.query.all()
    if data:
        info = [{"id": record.id,
                 "url": record.url,
                 "uid": record.uid,
                 "created_date": record.created_date} for record in data]
        return make_response(render_template("info.html", data=info, table_style="table"), 200)
    flash("There is no links data", category='info')
    return make_response(render_template("info.html"), 200)


@app.route("/get_url", methods=["POST", "GET"])
def get_url_by_id():
    if request.method == "POST":
        uid = Urls.query.filter_by(uid=request.form.get("uid")).first()
        if not uid:
            flash("There is no link for the given id or id is incorrect!", category="danger")
            return redirect(url_for('get_url_by_id'))
        flash("Found url!", category="success")
        return make_response(render_template("get.url.html", link=uid.url), 200)
    return make_response(render_template("get.url.html"), 200)


if __name__ == '__main__':
    db.create_all()
    app.run()
