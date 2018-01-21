# 返回晒美图详情的api
from flask import request

from plant.extensions import api, Resource, db
from plant.models import User, Beauti_essay, Beau_image, Beau_comment


class Beau_be(Resource):
    def post(self):
        #得到前段传来的数据
        page=request.json.get('page')

        #分页查询文章
        essays=Beauti_essay.query.order_by(db.desc(Beauti_essay.id))

        try:
            page_essays=essays.paginate(page=page,per_page=10)
        except:
            return {'code': 404, 'msg': '没有数据', 'data': None}

        # 创建data列表，用来存储返回每个文章组成的字典
        data = []
        #得到一页的具体数据
        essays_list=page_essays.items
        #遍历列表，然后得到所有具体的查询对象
        for one_essay in essays_list:
            #建立一个晒美图的字典
            be_dict={}
            #得到这篇晒美图的发帖用户
            user=one_essay.user
            #根据这个用户查询用户的头像和用户名
            be_dict['user_icon']=user.image
            be_dict['user_name']=user.nickname
            #得到晒美图的这个id
            be_dict['essay_id']=one_essay.id
            #得到晒美图的发帖时间
            be_dict['time']=one_essay.time.strftime('%Y-%m-%d %H:%M:%S')
            #得到晒美图的文字内容
            be_dict['essay']=one_essay.intro
            #得到晒美图的图片列表
            images=one_essay.image.all()
            images_list=[]
            for one_image in images:
                images_list.append(one_image.url)

            be_dict['images']=images_list
            #得到所有的评论
            comments_list=[]    #评论列表
            comments=one_essay.comment.all()
            for one_comment in comments:
                #一条评论组成的字典
                one_comment_dict={}
                one_comment_dict['comment']=one_comment.comment
                one_comment_dict['cuser_name']=one_comment.user.nickname
                comments_list.append(one_comment_dict)

            be_dict['comment']=comments_list
            #将这个晒美图的相关内容添加到data列表中
            data.append(be_dict)

        return {"code":200,"msg":"成功返回晒美图数据","data":data}


api.add_resource(Beau_be,'/api/v1/home/beau_essay')