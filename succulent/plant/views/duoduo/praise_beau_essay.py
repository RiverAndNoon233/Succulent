
#晒美图的点赞功能

from flask import request

from plant.extensions import api, Resource, db
from plant.models import User, Beauti_essay, Beau_image

class Prai_beau_essay(Resource):
    def post(self):
        #得到前端传来的json数据
        post_id=request.json.get('post_id')
        user_id=request.json.get('user_id')

        #根据用户的id查询用户
        user=User.query.get(user_id)

        #查询用户点赞过的文章列表，如果已经点过赞，则取消此次点赞
        pd_bes=user.prais_basu_img.all()
        #遍历，如果出现重复的id,则判断已经点过赞
        for one_be in pd_bes:
            if one_be.id ==post_id:
                return {"code":404,"msg":"点赞失败，已经点过赞了"}

        #根据文章id查询文章的id
        be=Beauti_essay.query.get(post_id)
        # 添加点赞关联
        user.prais_basu_img.append(be)
        #添加晒美图的点赞数量
        be.praise_num=be.praise_num+1
        #提交保存
        db.session.add(be)

        return {"code":200,"msg":"点赞成功"}

api.add_resource(Prai_beau_essay,'/api/v1/home/beau/praise')


