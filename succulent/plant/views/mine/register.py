# coding: utf-8
from flask import Blueprint, render_template, flash, redirect, url_for, request, current_app
# from plant.forms import RegisterForm, LoginForm, ModiUserForm, IconForm, FoundPasswd, ChangeMailForm
from plant.models import User
from plant.extensions import db
from plant.email import send_mail
from flask import jsonify

regist = Blueprint('register', __name__)
@regist.route('/register/', methods=['POST'])
def register():
    account = request.get_json(True).get('username')
    email = request.get_json(True).get('email')
    password = request.get_json(True).get('password')
    # print('account:',account,'email:','email','password:',password, '==========================')
    # 创建用户对象
    user = User()
    user.account = account
    user.passwd_hash = password
    # user.email = email
    # 判断此用户是否已存在
    if User.query.filter_by(account=account).first():
        return jsonify({'code': 1, 'msg': '该用户已经存在,注册失败'})
    elif User.query.filter_by(email=email).first():
        return jsonify({'code': 2, 'msg': '此邮箱已注册,注册失败'})
    # db.session.add(user)
    # 此时数据还没有保存到数据库中，没有id字段值，下面生成token时需要使用id
    # 因此等请求结束再提交时来不及的，故需要手动提交
    # db.session.commit()
    token = user.generate_activate_token(account=account,password=password,email=email)
    # 这里卡壳了...........
    send_mail(email, '账户激活', 'email/activate', account=account, token=token)
    # 给出flash提示消息
    # flash('邮件已发送，请点击链接完成用户激活')
    return jsonify({'code': 0, 'msg': '激活邮箱已发送'})

# 账户的激活
@regist.route('/activate1/<token>',methods=['GET','POST'])
def activate(token):
    print(222)
    if User.check_activate_token(token):
        return '<p>注册成功</p>'
    else:
        return '<p>链接已失效</p>'



