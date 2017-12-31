from datetime import datetime
from plant.extensions import db


class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key=True)
    rid = db.Column(db.Integer,index=True,default=0)
    title = db.Column(db.String(128))
    content = db.Column(db.Text)
    # 分类
    category = db.Column(db.String)
    # 浏览量
    count = db.Column(db.Integer, default=0)
    timestamp = db.Column(db.DateTime,default=datetime.utcnow)
    #添加关联外键，‘表名.字段’
    uid = db.Column(db.Integer,db.ForeignKey('users.id'))

