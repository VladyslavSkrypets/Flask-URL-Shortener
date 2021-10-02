from __init__ import db
from utils.helpers import get_date


class Urls(db.Model):
    __tablename__ = 'Urls'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text(), unique=True, nullable=False)
    short_url = db.Column(db.String(100), unique=True, nullable=False)
    uid = db.Column(db.String(8), unique=True, nullable=False)
    created_date = db.Column(db.DateTime, default=get_date(current=True))
    expire_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, url: str, short_url: str, uid: str, days_left: int):
        self.url = url
        self.uid = uid
        self.short_url = short_url
        self.expire_at = get_date(current=False, days=days_left)

    def __repr__(self):
        return f"<Urls {self.url}, {self.uid}>"
