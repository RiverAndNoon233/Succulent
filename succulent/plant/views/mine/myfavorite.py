from flask import Blueprint, request
from plant.models import User,Posts
from ..common.loginChecking import loginCheck

from flask import jsonify

myfavorite = Blueprint('myfavorite', __name__)

@myfavorite.route('/myfavorite/', methods=['POST'])
# @loginCheck
def myfp():
    uid = request.get_json(True).get('uid')
    user = User.query.filter_by(id=uid).first()
    data=[]
    for posts in user.favorite:
    ########   卡壳了    ###########
        data1 = {
            'id': posts.id,
            'title': posts.title,
            'content': posts.content,
            'category': posts.category,
            'count': posts.count,
            'timestamp': posts.timestamp,
        }
        data.append(data1)
        print(data)

    return jsonify({'code': 200, 'msg': 'success', 'data': data})
