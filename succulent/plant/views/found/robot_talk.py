#多多聊天机器人api

import json

from flask import request
from flask_restful import Resource

from plant.extensions import api
from plant.models import Posts
from plant.views.found.talk_robot import Talk_robot


class Robot_talk_API(Resource):
    def post(self):
        #得到前端传过来的json数据
        user_id=request.json.get('user_id')
        words=request.json.get('words')
        #实例化对象，调用方法：
        t=Talk_robot()
        robot_words=t.talk(str_words=words,user_id=user_id)

        return {"code":200,"msg":"对话成功","data":[{"robot_talk":robot_words}]}

api.add_resource(Robot_talk_API,'/api/v1/talk')