import uuid
from models import Urls
from __init__ import app, db
from flask import render_template, request, redirect, make_response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        long_url = request.form.get('long-url')
        url_exist = Urls.query.get()
        if not url_exist:
            url_uid = str(uuid.uuid4())[:10]

            db.session.add(Urls(original_url=long_url, url_uid=url_uid))
            db.session.commit()
        else:
            url_uid = url_exist

        short_url = f"{request.host_url}{url_uid}"

        return make_response(render_template("index.html", short_url=short_url), 201)

    return make_response(render_template("index.html"), 200)


@app.route("/<url_uid>")
def url_redirect(url_uid):
    url = Urls.query.filter(Urls.url_uid == url_uid).first()
    print(url)
    return "redirect(url)"


@app.route("/stat")
def statistic():
    pass


if __name__ == '__main__':
    db.create_all()
    app.run()
