from flask import Blueprint, request
from plant.models import User
from plant.email import send_mail
from flask import jsonify


change = Blueprint('change', __name__)

# 修改密码
@change.route('/changepd/', methods=['POST'])
def changepd():
    uid = request.get_json().get('uid')
    oldpd = request.get_json().get('old_password')
    newpd = request.get_json().get('new_password')

    # 查询此用户密码是否正确
    user = User.query.filter_by(id=uid).first()
    password = user.password
    if password == oldpd:
        user.password = newpd
        return jsonify({'code': 0, 'msg': '密码修改成功'})
    else:
        return jsonify({'code': 1, 'msg': '原密码输入错误'})

# 修改邮箱
@change.route('/changeEm/')
def changeEm():
    uid = request.get_json().get('uid')
    # oldpd = request.get_json().get('old_email')
    newEmail = request.get_json().get('new_email')

    # 查询此用户
    user = User.query.filter_by(id=uid).first()
    # 判断此邮箱是否已经注册
    if User.query.filter_by(email=newEmail).first():
        return jsonify({'code': 1, 'msg': '此邮箱已经注册'})
    else:
        # 发送验证邮件
        token = user.generate_activate_token(uid=user.id, email=newEmail)
        # 这里卡壳了...........
        send_mail(user.email, '账户激活', 'email/activate', account=user.account, token=token)
        return jsonify({'code': 0, 'msg': '发送邮箱验证'})

# 修改头像
@change.route('/changeIg/')
def changeIg():
    pass