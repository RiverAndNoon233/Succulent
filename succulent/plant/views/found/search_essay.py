#<<<<<<< HEAD
#=======
#搜索文章api

#>>>>>>> 46c4c5f92bb716186771010d5fb5f8ffc3bbaed5
from flask import  request
from sqlalchemy import or_

from plant.extensions import api, Resource, db, moment
from plant.models import User, Posts, Image

#主页搜索功能的API

class Search_essay_API(Resource):
    def post(self):
        # 得到文章的页码数
        page = request.json.get('page')
        #得到文章传来的搜索关键词
        words=request.json.get('words')
        # 分页查询文章,按照模糊查询，查询是否包含该关键词，查询文章标题和文章正文内容
        posts = Posts.query.filter(or_(Posts.title.contains(words),Posts.content.contains(words))).filter_by(rid=0)

        #判断文章输入的页数是否在正确的范围内，不在则返回404
        try:
            page_posts=posts.paginate(page=int(page),per_page=10)
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
            # 得到文章id
            one_data['id'] = one_post.id
            # 得到文章标题
            one_data['title'] = one_post.title

            # 得到文章的图片
            images = one_post.image
            # 判断文章是否有图片，如果有，则返回图片的第一张
            if len(list(images))!=0:
                one_image=images[0].url
            else:
                one_image=''
            #执行赋值
            one_data['urlimage'] = one_image
            # 得到文章时间
            one_data['timestamp'] = one_post.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            # 得到文章的浏览量
            one_data['count'] = one_post.count

            data.append(one_data)

        return {'code': 200, 'msg': '获取成功', 'data': data}

api.add_resource(Search_essay_API, '/api/v1/found/search_essay')
