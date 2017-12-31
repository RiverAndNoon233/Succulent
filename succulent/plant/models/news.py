from datetime import datetime
from plant.extensions import db


class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    rid = db.Column(db.Integer, index=True, default=0)
    title = db.Column(db.String(128))
    content = db.Column(db.Text)
    # 浏览量
    count = db.Column(db.Integer,default=0)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

