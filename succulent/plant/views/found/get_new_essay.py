# 发现里的最新文章

import datetime
import json

from flask import Blueprint, request

from plant.extensions import api, Resource, db, moment
from plant.models import User, Posts, Image

get_new_essay = Blueprint('get_new_essay', __name__)


class Get_new_essay_API(Resource):
    # post方法的api
    def post(self):
        # 得到文章的页码数
        page = request.json.get('page')
        # 分页查询文章
        posts = Posts.query.order_by(db.desc(Posts.timestamp)).filter_by(rid=0)
        print(page)
        try:
            page_posts = posts.paginate(page=page, per_page=10)
        except:
            return {'code': 404, 'msg': '没有数据', 'data': None}

        # 创建data列表，用来存储返回每个文章组成的字典
        data = []

        # 分析分页对象，得到分页对象中的具体数据，并把数据返回给调用者
        posts = page_posts.items
        for one_post in posts:
            # 得到对象的每一个值，然后以字典的形式存储，添加到data字典中
            one_data = {}
            # 得到这篇文章的用户对象
            user = one_post.user
            # 得到用户头像
            one_data['user_icon'] = user.image
            # 得到用户名
            one_data['user_name'] = user.nickname
            # 得到文章的id
            one_data['essay_id'] = one_post.id
            # 得到文章标题
            one_data['essay_title'] = one_post.title
            # 得到文章的图片
            images = one_post.image
            # 遍历图片得到前三张图片
            image_list = []
            i = 1
            for one_img in images:
                one_img_url = one_img.url
                image_list.append(one_img_url)
                i = i + 1
                if i > 3:
                    break
            one_data['essay_image'] = image_list
            # 得到文章时间
            one_data['essay_time'] = one_post.timestamp.strftime(
                '%Y-%m-%d %H:%M:%S')
            # 得到文章的浏览量
            one_data['essay_views_num'] = one_post.count

            data.append(one_data)

        return {'code': 200, 'msg': '获取成功', 'data': data}


api.add_resource(Get_new_essay_API, '/api/v1/found/new_essay')
