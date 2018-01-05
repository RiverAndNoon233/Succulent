from plant.extensions import db
from .users import User
from .posts import Posts
from .news import News
from .goods import Goods

# 创建多对多的中间关联表,ORM自动维护
collections = db.Table('collections',
                       db.Column('user_id',db.Integer,db.ForeignKey('users.id')),
                       db.Column('posts_id',db.Integer,db.ForeignKey('posts.id'))
                       )