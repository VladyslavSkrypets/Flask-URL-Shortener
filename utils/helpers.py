import string
import random
import pytz
import datetime


def get_date(current: bool = False, days: int = 0) -> str:
    if current:
        return pytz.utc.localize(datetime.datetime.utcnow()).strftime("%Y-%m-%d %H:%M:%S")
    return pytz.utc.localize(datetime.datetime.utcnow() + datetime.timedelta(days=days)).strftime("%Y-%m-%d %H:%M:%S")


def uid_generator() -> str:
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(8))


def url_expired(expire_at: datetime.datetime) -> bool:
    return expire_at <= datetime.datetime.strptime(get_date(current=True), "%Y-%m-%d %H:%M:%S")

