from flask import current_app, flash

from plant.extensions import db
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature,SignatureExpired
from plant.extensions import login_manager
# 导入密码散列及校验函数
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.String(120),unique=True)
    nickname = db.Column(db.String(120),default='小小肉')
    passwd_hash = db.Column(db.String(128))
    email = db.Column(db.String(128),unique=True,nullable=True)
    confirmed = db.Column(db.Boolean, default=False)
    # 头像
    image = db.Column(db.String(200), nullable=True)
    # 多币
    duocoin = db.Column(db.String(128),default=0)

    # 在另一模型中添加反向引用
    # 参数1：关联的模型名
    # 参数2：在关联的模型中动态添加的字段
    # 参数3：加载方式--dynamic，不加载，但是提供记录的查询
    # 一对多的关系
    posts = db.relationship('Posts', backref='user', lazy='dynamic')

    # 收藏的帖子
    favorite = db.relationship('Posts', secondary='favorite', backref=db.backref('users', lazy='dynamic'), lazy='dynamic')

    # 购物车 多对多
    shopping_car = db.relationship('Shoppingcar', secondary='shopping', backref=db.backref('users', lazy='dynamic'), lazy='dynamic')

    #用户评论新闻的关联
    comment = db.relationship('News_comment',backref='user',lazy='dynamic')

    # 若使用一对一，添加userlist=Flase
    # posts = db.relationship('Posts',backref='user',lazy='dynamic')

    # 可以保护某一个字段
    @property
    def password(self):
        raise AttributeError('密码是不可读属性')

    # 设置密码，加密存储
    @password.setter
    def password(self, password):
        self.passwd_hash = generate_password_hash(password)

    # 密码校验
    def verify_password(self, password):
        return check_password_hash(self.passwd_hash,password)

    # 生成激活的token
    def generate_activate_token(self, expires_in=3600,uid=None,account=None,password=None, email=None):
        # 创建用于生成token的类，需要传递密钥和有效期
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expires_in)

        # 生效包含有效信息(必须是字典数据)的token字符串
        return s.dumps({'id': self.id, 'email':email,'uid':uid,'account':account,'password':password})

    # 找回密码的token
    def foundpw_activate_token(self, expires_in=3600, passwd=None, email=None):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expires_in)
        return s.dumps({'passwd':passwd, 'email':email})
    # 找回密码的激活账户方法
    def checkpw_activate_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except BadSignature:
            flash('无效的token')
            return False
        except SignatureExpired:
            flash('token已失效')
            return False
        user = User.query.filter_by(email=data.get('email')).first()

        user.password = (data.get('passwd'))
        db.session.add(user)
        return True

    # 账号激活，因为激活时还不知道是哪个用户
    @staticmethod
    def check_activate_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except BadSignature:
            flash('无效的token')
            return False
        except SignatureExpired:
            flash('token已失效')
            return False
        user = User()
        user.confirmed = True
        user.email = data.get('email')
        user.passwd_hash = generate_password_hash(data.get('password'))
        user.account = data.get('account')
        db.session.add(user)
        return True

    # 修改邮箱的激活
    @staticmethod
    def change_email_activate_token(token):
        print('=========================')
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except BadSignature:
            # flash('无效的token')
            return False
        except SignatureExpired:
            # flash('token已失效')
            return False
        print(data.get('uid'),'======================')
        user = User.query.filter_by(id=data.get('uid')).first()
        user.email = data.get('email')
        db.session.add(user)
        return True



    # 判断是否收藏了指定帖子
    def is_favorite(self,pid):
        # 获取该用户收藏的所有帖子
        favorites = self.favorites.all()
        # 判断是否收藏
        posts = list(filter(lambda p: p.id == pid,favorites))
        if len(posts) > 0:
            return True
        return False
    # 收藏指定帖子
    # def add_favorite(self, pid):
    #     p = Posts.query.get(pid)
    #     self.favorites.append(p)
    # 取消收藏
    # def rm_favorite(self, pid):
    #     p = Posts.query.get(pid)
    #     self.favorites.remove(p)

# 登录认证的回调
@login_manager.user_loader
def load_user(uid):
    return User.query.get(int(uid))