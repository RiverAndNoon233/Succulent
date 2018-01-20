from plant.views.duoduo.main import main
from plant.views.found.get_new_essay import get_new_essay
from plant.views.found.writepublish import writepublish
from plant.views.mine.login import login
from plant.views.mine.register import regist
from plant.views.mine.change import change
from plant.views.mine.myfavorite import myfavorite
from plant.views.duoduo.news import index
from plant.views.mine.foundpd import found

# <<<<<<< HEAD
# <<<<<<< HEAD
# <<<<<<< HEAD
from plant.views.mine.myposts import myposts
# =======
# =======
# >>>>>>> be85942f0d714ed59c0d69d143a763b7dcaa1b5b
# =======
# >>>>>>> be85942f0d714ed59c0d69d143a763b7dcaa1b5b
# <<<<<<< HEAD
# from plant.views.shop.shop import shop
# =======
from plant.views.shop.shop import shop
# >>>>>>> 2501b6d5a12b459ad381b2a09d9a6a605b114d79

# >>>>>>> 7f7e5be0508532fdedeb556641b4b58cef196c08
#蓝本配置

DEFAULT_BLUEPRINT = (
    (main, ''),
    (login, '/api/v1/user'),
    (regist, '/api/v1/user'),
    (myposts,'/api/v1/user'),
    (myfavorite,'/api/v1/user'),
    (change,'/api/v1/user'),
    (found,'/api/v1/user'),
    (shop, '/api/v1/shop'),
    (writepublish,'/api/v1/writepublish'),
    (get_new_essay,'/api/v1/found/get_new_essay'),
    (index, '/api/v1/index'),


)

#封装函数，完成蓝本注册
def config_blueprint(app):
    for blueprint,prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint,url_prefix=prefix)
