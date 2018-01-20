from flask import Blueprint, request,session,redirect,url_for
from plant.models import User
from plant.email import send_mail
from flask import jsonify
from plant.extensions import db
from flask_login import login_user, logout_user, login_required, current_user
from ..common.loginChecking import loginCheck
change = Blueprint('change', __name__)

# 修改密码
@change.route('/changepd/', methods=['POST'],endpoint='changepd')
# @loginCheck
def changepd():
    # print('session:',session.get('session_id'))
    uid = request.get_json(True).get('uid')
    oldpd = request.get_json(True).get('old_password')
    newpd = request.get_json(True).get('new_password')
    user = User.query.filter_by(id=uid).first()
    print(uid,"============================")
    if user.verify_password(oldpd):
        user.password = newpd
        db.session.add(user)
    # 查询此用户密码是否正确
        return jsonify({'code': 0, 'msg': '密码修改成功'})
    else:
        return jsonify({'code': 1, 'msg': '原密码输入错误'})

# 修改邮箱
@change.route('/changeEm/',methods=['POST'],endpoint='changeEm')
# @loginCheck
def changeEm():
    uid = request.get_json(True).get('uid')
    # oldpd = request.get_json().get('old_email')
    newEmail = request.get_json(True).get('new_email')

    # 查询此用户
    user = User.query.filter_by(id=uid).first()
    # 判断此邮箱是否已经注册
    if User.query.filter_by(email=newEmail).first():
        return jsonify({'code': 1, 'msg': '此邮箱已经注册'})
    else:
        # 把需要的信息塞到token里
        token = user.generate_activate_token(uid=user.id, email=newEmail)
        # 发送验证邮件
        send_mail(newEmail, '账户验证', 'email/change_email_activate', token=token)
        return jsonify({'code': 0, 'msg': '发送邮箱验证'})

# 账户的激活
@change.route('/activate2/<token>', methods=['GET', 'POST'])
def activate(token):
    print(111)
    if User.change_email_activate_token(token):
        return "<p>邮箱修改成功</p>"
    else:
        return jsonify({'code': 1, 'msg': '链接已失效'})

# 修改头像
@change.route('/changeIg/',endpoint='changeIg')
# @loginCheck
def changeIg():
    pass