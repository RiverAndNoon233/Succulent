from flask import Blueprint, request
from plant.models import Posts
from flask import jsonify
from ..common.loginChecking import loginCheck

myposts = Blueprint('myposts', __name__)


@myposts.route('/myposts/', methods=['POST'])
# @loginCheck
def mypost():
    uid = request.get_json('uid').get('uid')
    data = []
    for posts in Posts.query.filter_by(uid=uid):
        data1 = {
            'essay_id': posts.id,
            'essay_title': posts.title,
            'essay': posts.content,
            'category': posts.category,
            'essay_views_num': posts.count,
            'essay_time': posts.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        }
        data.append(data1)
    return jsonify({'code': 200, 'msg': 'success', 'data': data})