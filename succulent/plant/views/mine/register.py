import os
from flask import Blueprint, render_template, flash, redirect, url_for, request, current_app
# from plant.forms import RegisterForm, LoginForm, ModiUserForm, IconForm, FoundPasswd, ChangeMailForm
from plant.models import User
from plant.extensions import db
from plant.email import send_mail
from flask import jsonify

regist = Blueprint('register', __name__)
@regist.route('/regist/', methods=['POST'])
def register():
    account = request.get_json().get('account')
    email = request.get_json().get('email')
    password = request.get_json().get('password')
    # 创建用户对象
    user = User.objects(account=account)
    # 判断此用户是否已存在
    if user:
        return jsonify({'code': 1, 'msg': '该用户已经存在,注册失败'})
    if User.query.filter_by(email=email).first():
        return jsonify({'code': 2, 'msg': '此邮箱已注册,注册失败'})

    user.account = account
    user.password = password
    # user.email = email
    db.session.add(user)
    # 此时数据还没有保存到数据库中，没有id字段值，下面生成token时需要使用id
    # 因此等请求结束再提交时来不及的，故需要手动提交
    db.session.commit()
    token = user.generate_activate_token(uid=user.id,email=email)
    # 这里卡壳了...........
    send_mail(user.email, '账户激活', 'email/activate', account=account, token=token)
    # 给出flash提示消息
    # flash('邮件已发送，请点击链接完成用户激活')
    return jsonify({'code': 0, 'msg': '注册成功'})

# 账户的激活  =================需要完善====================
# @regist.route('/activate/<token>',methods=['GET','POST'])
# def activate(token):
#     if User.check_activate_token(token):
#         return redirect(url_for('user.login'))
#     else:
#         return redirect(url_for('main.index'))



