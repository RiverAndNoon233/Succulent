from datetime import datetime

from plant.extensions import db


class Beauti_essay(db.Model):
    __tablename__='beauti_essay'
    id = db.Column(db.Integer, primary_key=True)
    #简介
    intro=db.Column(db.String(1000))

    #晒美图的时间
    time=db.Column(db.DateTime,default=datetime.utcnow)

    # 添加关联外键，‘表名.字段’
    uid = db.Column(db.Integer, db.ForeignKey('users.id'))

    #晒美图的点赞数量
    praise_num=db.Column(db.Integer,default=0)

    #关联晒美图的评论
    comment=db.relationship('Beau_comment',backref='beau_essay', lazy='dynamic')

    # 关联晒美图的图片一对多关系
    image = db.relationship('Beau_image', backref='beau_essay', lazy='dynamic')


class Beau_image(db.Model):
    __tablename__ = 'beau_image'
    id = db.Column(db.Integer, primary_key=True)

    url=db.Column(db.Text)

    #关联晒美图一对多外键,beau_photo实际上指的是Beauti_essay这个表.
    beau_photo = db.Column(db.Integer, db.ForeignKey('beauti_essay.id'))

class Beau_comment(db.Model):
    __tablename__='beau_comment'
    id=db.Column(db.Integer, primary_key=True)
    comment=db.Column(db.Text)

    #关联晒美图一对多外键
    beau_esssay = db.Column(db.Integer, db.ForeignKey('beauti_essay.id'))

    #关联用户外键
    u=db.Column(db.Integer,db.ForeignKey('users.id'))
