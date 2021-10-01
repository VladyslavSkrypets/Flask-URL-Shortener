import datetime
from __init__ import db


class Urls(db.Model):
    __tablename__ = 'Urls'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text(), unique=True, nullable=False)
    uid = db.Column(db.String(10), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    def __init__(self, url: str, uid: str):
        self.url = url
        self.uid = uid

    def __repr__(self):
        return f"<Urls {self.url}, {self.uid}>"
