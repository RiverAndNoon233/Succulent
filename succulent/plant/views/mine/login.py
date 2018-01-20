from flask import Blueprint, request, render_template, session
from plant.models import User

from flask import jsonify

login = Blueprint('login', __name__)


@login.route('/login/', methods=['POST'])
def logined():
    # 获取通过url请求传参的数据
    account = request.get_json(True).get('account')
    # print(account)
    # 获取url请求传的密码，明文
    password = request.get_json(True).get('password')
    # 判断用户名、密码都不为空，如果不传用户名、密码则account和password为None
    if account and password:
        # 查询账号是否存在且密码是否与之匹配
        user = User.query.filter_by(account=account).first()
        if not user:
            return jsonify({'code': 1, 'msg': '登陆失败,此用户不存在'})
        elif not user.verify_password(password):
            # print(user.passwd_hash)
            return jsonify({'code': 2, 'msg': '登录失败,密码输入错误'})
        elif user.confirmed == False:
            return jsonify({'code': 3, 'msg': '登录失败,用户邮箱未激活'})
        session['session_id'] = user.id
        print(session.get('session_id'))
        # session.pop('session_id', None)
        # print(session.get('session_id'))
        # 以上都没错误 返回用户id
        data = {
            "uid":user.id,
            # "account": user.account,  # 账号
            # "password": user.password,
            "nickname": user.nickname,  # 昵称
            # "email": user.email,  # 邮箱
            # "confirmed": user.confirmed,  # 邮箱是否已验证激活
            # "image": user.image,  # 头像
            "duocoin":user.duocoin,# 多币
            # "posts":user.posts,
            # "favorite":user.favorite,
            # "shopping_car":user.shopping_car,
        }
        return jsonify({'code': 0, 'msg':'登录成功','data':data })
