from __init__ import ma


class UrlsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ("id", "url", "uid", "short_url", "created_date", "expire_at")


url_schema = UrlsSchema()
urls_schema = UrlsSchema(many=True)
