from datetime import datetime
from plant.extensions import db


class Goods(db.Model):
    __tablename__ = 'goods'
    id = db.Column(db.Integer,primary_key=True)
    good_name = db.Column(db.String(128))
    #价格
    price = db.Column(db.Float)
    # 简介
    introduction = db.Column(db.Text)
    #图片
    image = db.Column(db.String(256),nullable=True)
    # 分类
    category = db.Column(db.String)



class Shoppingcar(db.Model):
    __tablename__ = 'shoppingcar'
    id = db.Column(db.Integer, primary_key=True)
    gid = db.Column(db.Integer)
    #数量
    num = db.Column(db.Integer,default=0)
    #用户
    uid = db.Column(db.Integer,db.ForeignKey('users.id'))

