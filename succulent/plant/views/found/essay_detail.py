# 展示发现里的文章详情

from flask import Blueprint, request

from plant.extensions import api, Resource, db, moment
from plant.models import User, Posts, Image


class Essay_detail_API(Resource):
    def post(self):
        # 得到用户传入的id
        essay_id = request.json.get('essay_id')
        # 根据用户的id获取相应文章的数据：
        post = Posts.query.get(essay_id)

        # 判断，如果获取文章为空，则返回404错误
        if not post:
            return {'code': 404, 'msg': '没有获取到数据', 'data': None}

        # 并把文章的浏览量加1：
        post.count = post.count + 1
        db.session.add(post)

        # 得到这个文章的相关信息，并组成一个字典
        post_dict = {}
        post_dict['essay_id'] = post.id
        post_dict['essay_title'] = post.title
        post_dict['essay_views_num'] = post.count
        post_dict['essay_time'] = post.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        post_dict['essay'] = post.content
        # 获取文章图片的所有图片列表
        images = post.image
        images_url_list = []
        for one in images:
            images_url_list.append(one.url)
        post_dict['essay_image'] = images_url_list

        # data数据集合：
        data = [post_dict]

        return {'code': 200, 'msg': '成功得到数据', 'data': data}


api.add_resource(Essay_detail_API, '/api/v1/found/essay_detail')
