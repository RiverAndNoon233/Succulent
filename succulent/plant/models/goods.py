from datetime import datetime
from plant.extensions import db


class Goods(db.Model):
    __tablename__ = 'goods'
    id = db.Column(db.Integer,primary_key=True)
    
    good_name = db.Column(db.String(128))
    #价格
    price = db.Column(db.Float)
    # 简介
    introduction = db.Column(db.Text())
    #图片
    images = db.relationship('Goods_img', backref='good', lazy='dynamic')
    # 分类
    category = db.Column(db.String)
    #购买次数
    count = db.Column(db.Integer)



class Shoppingcar(db.Model):
    __tablename__ = 'shoppingcar'
    id = db.Column(db.Integer, primary_key=True)
    gid = db.Column(db.Integer)
    #数量
    num = db.Column(db.Integer,default=0)
    #用户
    uid = db.Column(db.Integer,db.ForeignKey('users.id'))




class Goods_img(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     #图片
     img = db.Column(db.String(256))
     #一对多关联
     goods = db.Column(db.Integer,db.ForeignKey('goods.id'))