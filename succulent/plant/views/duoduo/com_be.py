
#晒美图的评论的api


from flask import request

from plant.extensions import api, Resource, db
from plant.models import User, Beauti_essay, Beau_image, Beau_comment


class Com_be(Resource):
    def post(self):
        #得到前段传来的数据
        user_id = request.json.get('user_id')
        post_id = request.json.get('post_id')
        comment = request.json.get('comment')

        #根据user_id查询得到用户
        user=User.query.get(user_id)
        #根据post_id查询得到被评论的晒美图
        be=Beauti_essay.query.get(post_id)

        #实例化一个评论对象
        bc=Beau_comment()
        #设置他的评论内容
        bc.comment=comment
        #设置他的评论的美图文章
        bc.beau_essay=be
        #设置评论他的用户
        bc.user=user

        db.session.add(bc)

        return {"code":200,"msg":"发表评论成功"}



api.add_resource(Com_be,'/api/v1/home/beau_photo/comment')