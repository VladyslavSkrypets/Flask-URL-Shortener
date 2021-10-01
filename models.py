import datetime
from __init__ import db


class Urls(db.Model):
    __tablename__ = 'Urls'

    id = db.Column(db.Integer, primary_key=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    original_url = db.Column(db.Text())
    url_uid = db.Column(db.String(10))

    def __init__(self, original_url: str, url_uid: str):
        self.original_url = original_url
        self.url_uid = url_uid
