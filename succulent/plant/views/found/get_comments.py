#获取文章的所有评论

import json

from flask import request
from flask_restful import Resource

from plant.extensions import api
from plant.models import Posts


class Get_comments_API(Resource):
    def post(self):
        #得到传入的数据
        essay_id=request.json.get('essay_id')
        #得到该文章下的所有评论
        comments=Posts.query.filter_by(rid=essay_id)
        #判断如果获取不到数据，则发挥404
        if len(list(comments))==0:
            return {'code':404,'msg':'没有获取数据','data':None}

        #数据列表
        data=[]
        for one_comment in comments:
            one_data={}
            user=one_comment.user
            #得到该评论下用户的ID,用户头像、用户名
            one_data['user_id']=user.id
            one_data['user_icon']=user.image
            one_data['user_name']=user.nickname
            #得到文章的评论时间、评论正文
            one_data['comment_time']=one_comment.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            one_data['comment']=one_comment.content
            one_data['comment_id']=one_comment.id

            data.append(one_data)

        return {'code':200,'msg':'成功获取信息','data':data}

api.add_resource(Get_comments_API,'/api/v1/found/show_comment')