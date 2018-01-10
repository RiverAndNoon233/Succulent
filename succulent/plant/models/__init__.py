from plant.extensions import db
from .users import User
from .posts import Posts
from .news import News
from .goods import Goods
from .images import Image

# 创建多对多的中间关联表,ORM自动维护
favorite = db.Table('favorite',
                       db.Column('user_id',db.Integer,db.ForeignKey('users.id')),
                       db.Column('posts_id',db.Integer,db.ForeignKey('posts.id'))
                       )
shopping = db.Table('shopping',
                       db.Column('user_id',db.Integer,db.ForeignKey('users.id')),
                       db.Column('Shoppingcar_id',db.Integer,db.ForeignKey('shoppingcar.id'))
                       )
