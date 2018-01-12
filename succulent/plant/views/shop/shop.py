from flask import Blueprint,request,jsonify
from plant.models.goods import Goods,Shoppingcar
from plant.models.users import User
from plant.extensions import db


shop = Blueprint('shop',__name__)

#商品列表
@shop.route('/showgoods/')
def showgoods():
    ll = []
    category = request.args.get('category')
    page = request.args.get('page', 1, int)
    if category is None:
         category = '1'

    paginates = Goods.query.filter_by(category=category).paginate(page,per_page=20,error_out=False)
    goods = paginates.items
    for i in goods:
        dic = {'goods_name':i.good_name,'gid':i.id,'price':i.price,'image':i.image}
        ll.append(dic)


    return jsonify(ll)


#商品详情
@shop.route('/goods_details/')
def goods_details():
    gid = request.args.get('gid')
    if gid is None:
        return jsonify({'code':0,'msg':404})
    goods = Goods.query.get(gid)
    if goods is None:
        return jsonify({'code':0,'msg':404})
    
    return jsonify({'goods_name':goods.good_name,'gid':goods.id,'price':goods.price,'image':goods.image,'introduction':goods.introduction})

#购物车页面
@shop.route('/myshop_car/')
def show_car():
    uid = request.args.get('uid')
    if uid is not None:
        car_list= []
        user = User.query.get(uid)
        cars = user.shopping_car.all()
        for car in cars:
            g = Goods.query.get(car.gid)
            allprice = g.price*car.num
            data = {'id':g.id,'name':g.good_name,'num':car.num,'price':g.price,'allprice':allprice}
            car_list.append(data)
        return jsonify({'code':1,'msg':'success','data':car_list})
    return jsonify({'code':0,'msg':'failure'})

#增删购物车collections
@shop.route('/add_del_car/')
def add_del_car():
    uid = request.args.get('uid')
    gid = request.args.get('gid')
    ad = request.args.get('ad')
    if uid is not None:
        if ad == '1':
            user = User.query.get(uid)
            car = user.shopping_car.filter_by(gid = gid)
            print(type(car))
            if len(list(car)) == 1 :
                # num =  car[0].num
                car[0].num +=1
                # db.session.add(car)
                return jsonify({'data':1})
            car = Shoppingcar(gid = gid,num = 1,uid = uid)
            user.shopping_car.append(car)
            db.session.add(car)

            return jsonify({'data':1})
        if ad == '0':
            user = User.query.get(uid)
            car = user.shopping_car.filter_by(gid=gid)
            print(len(list(car)))
            if len(list(car))==1 :
                if  car[0].num > 1:
                    car[0].num -= 1
                    return jsonify({'data': 1})
                c = Shoppingcar.query.filter_by(gid = car[0].gid).first()

                db.session.delete(c)
                print('delete')
                return jsonify({'data': 1})
    return jsonify({'data': 0})
