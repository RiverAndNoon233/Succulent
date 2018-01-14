from flask import session,redirect,url_for,jsonify

# class LoginChecking():
#     @classmethod
def loginCheck(func):
    def check():
        if session.get('session_id'):
            print('已经登录')
            return func
        else:
            print('跑去登录页面')
            return jsonify({'code':200,'msg':'未登录跳转登录'})
    return check