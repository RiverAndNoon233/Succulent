# 发现里的评论书写

import json

from flask import Blueprint, request

from plant.extensions import api,  db, moment
from plant.models import User, Posts, Image
from flask_restful import Resource

class Write_comment_API(Resource):
    def post(self):
        #得到数据
        user_id=request.json.get('comment_user_id')
        essay_id=request.json.get('essay_id')
        comment=request.json.get('comment')
        #查询得到具体用户
        user=User.query.get(user_id)
        #执行保存操作：
        p=Posts()
        p.rid=int(essay_id)
        p.content=comment
        p.user=user
        db.session.add(p)

        return {'code':200,'msg':'评论发表成功'}

api.add_resource(Write_comment_API,'/api/v1/found/wirtecomment')