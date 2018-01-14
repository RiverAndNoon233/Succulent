from datetime import datetime
from plant.extensions import db


class News(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    # 文章标题
    title = db.Column(db.String(128), unique=True)
    # 正文内容
    content = db.Column(db.Text)
    # 浏览量
    count = db.Column(db.Integer, default=0)
    # 时间戳
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    # 关联图片一对多关系
    images = db.relationship('News_image', backref='newsid', lazy='dynamic')
    # 评论
    comment = db.relationship('News_comment', backref='c_news', lazy='dynamic')


class News_image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # 图片
    img = db.Column(db.String(256))
    # 关联外键
    news_id = db.Column(db.Integer, db.ForeignKey('news.id'))


class News_comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # 评论内容
    context = db.Column(db.String(1024))
    # 评论时间
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    # 文章关联
    news_id = db.Column(db.Integer, db.ForeignKey('news.id'))
    # 用户关联
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
