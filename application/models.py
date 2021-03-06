from application import db
from datetime import datetime
import pytz

def utcnow():
    return datetime.now(tz=pytz.utc)

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50), nullable=False)
    complete = db.Column(db.Boolean, nullable=False, default=False)
    date_created = db.Column(db.DateTime, nullable=False, default=utcnow())