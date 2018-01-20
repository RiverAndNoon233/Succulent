
#发表晒美图

from flask import request

from plant.extensions import api, Resource, db
from plant.models import User, Beauti_essay, Beau_image


class Write_beauti_img(Resource):
    def post(self):
        #获取前端传过来的值
        user_id=request.json.get('user_id')
        intro=request.json.get('intro')
        images=request.json.get('images')

        print(images)

        if images is None:
            return {"code":404,"msg":"图片不能为空"}

        # 查询出发帖用户
        user = User.query.filter_by(id=int(user_id)).first()

        #实例化晒美图类，然后执行添加操作
        be=Beauti_essay()
        be.intro=intro
        be.user=user
        db.session.add(be)

        #实例化图片类，然后进行保存图片的操作
        for one_image in images:
            bi=Beau_image()
            bi.url=one_image
            #按照id降序查询beau_essay，取最后一个
            last_be=Beauti_essay.query.order_by(db.desc(Beauti_essay.id)).first()
            bi.beau_essay=last_be
            db.session.add(bi)

        return {"code":200,"msg":"发表晒美图成功"}



api.add_resource(Write_beauti_img,'/api/v1/beauphoto/publish')