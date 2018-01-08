from flask import Blueprint, request
from plant.models import User

from flask import jsonify

myposts = Blueprint('myposts', __name__)


@myposts.route('/myposts/', methods=['GET'])
def myposts():
    uid = request.get_json().get('uid')
    user = User.query.filter_by(fid=uid).first()
    data = user.favorite

    ########   卡壳了    ###########
    # data = {
    #     'id': posts.id,
    #     'title': posts.title,
    #     'content': posts.content,
    #     'category': posts.category,
    #     'count': posts.count,
    #     'timestamp': posts.timestamp,
    # }
    return jsonify({'code': 200, 'msg': 'success', 'data': data})

