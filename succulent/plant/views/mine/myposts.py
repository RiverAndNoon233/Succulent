from flask import Blueprint, request
from plant.models import Posts

from flask import jsonify

myposts = Blueprint('myposts', __name__)


@myposts.route('/myposts/', methods=['POST'])
def mypost():
    uid = request.get_json().get('uid')
    posts = Posts.query.filter_by(uid=uid)
    data = {
        'id': posts.id,
        'title': posts.title,
        'content': posts.content,
        'category': posts.category,
        'count': posts.count,
        'timestamp': posts.timestamp,
    }
    return jsonify({'code': 200, 'msg': 'success', 'data': data})