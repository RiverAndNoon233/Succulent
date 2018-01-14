from datetime import datetime
from plant.extensions import db


class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key=True)
    rid = db.Column(db.Integer,index=True,default=0)
    #文章标题
    title = db.Column(db.String(128),unique=True)
    #正文内容
    content = db.Column(db.Text)
    # 分类
    category = db.Column(db.String)
    # 浏览量
    count = db.Column(db.Integer, default=0)
    #点赞量：
    praise_num=db.Column(db.Integer,default=0)
    #时间戳
    timestamp = db.Column(db.DateTime,default=datetime.utcnow)
    #添加关联外键，‘表名.字段’
    uid = db.Column(db.Integer,db.ForeignKey('users.id'))

    #关联图片一对多关系
    image = db.relationship('Image', backref='post', lazy='dynamic')

