#发现里发表文章

from flask import Blueprint, request

from plant.extensions import api, Resource, db
from plant.models import User, Posts, Image

writepublish = Blueprint('writepublish', __name__)

class WritepublishAPI(Resource):
    #post方法的api
    def post(self):
        #文章类别
        kind=request.json['kind']
        #文章标题
        title=request.json['title']
        #文章正文
        essay=request.json['essay']
        #用户id
        user_id=request.json['user_id']
        #查询出发帖用户
        user=User.query.filter_by(id=int(user_id)).first()
        # print(user.nickname)
        #获取图片：
        try:
            images=request.json['image']
        except:
            images=None

        #如果数据库中已经存在这个标题，则返回503
        if Posts.query.filter_by(title=title).first():
            return {'code': 503, "msg": "标题已经存在"}
        #执行数据库存取：
        #存文章
        p=Posts()
        p.title=title
        p.category=kind
        p.content=essay
        p.user=user

        # 执行保存文章的方法
        db.session.add(p)

        try:
            # 如果图片不为空，则执行存储操作
            if  images:
                for one_image in images:
                    img = Image()
                    img.url = one_image
                    post=Posts.query.filter_by(title=title).first()
                    # print(post)
                    img.post=post
                    db.session.add(img)
            return {'code':200,'msg':'success'}
        except:
            return {'code':503,'msg':'failed'}

api.add_resource(WritepublishAPI,'/api/v1/found/writepublish')