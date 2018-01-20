# coding: utf-8
from flask import Blueprint, render_template, flash, redirect, url_for, request, current_app
from plant.models import User
from plant.extensions import db
from plant.email import send_mail
from flask import jsonify

found = Blueprint('foundpd', __name__)

@found.route('/foundpd/', methods=['POST'])
def foundpd():
    email = request.get_json(True).get('email')
    password = request.get_json(True).get('password')
    # print('email:','email','password:',password, '==========================')
    # 创建用户对象
    # 判断此邮箱是否正确
    user = User.query.filter_by(email=email).first()
    if user:
        token = user.foundpw_activate_token(passwd=password,email=email)
        # 这里卡壳了...........
        send_mail(email, '账户激活', 'email/foundpd', token=token)
        # 给出flash提示消息
        # flash('邮件已发送，请点击链接完成用户激活')
        return jsonify({'code': 0, 'msg': '重置密码邮件已发送'})
    else:
        return jsonify({'code': 1, 'msg': '此邮箱不存在'})

# 重置密码邮件验证
@found.route('/activate3/<token>',methods=['GET','POST'])
def activate(token):

    if User.checkpw_activate_token(token):
        return '<p>密码重置成功</p>'
    else:
        return '<p>链接已失效</p>'



