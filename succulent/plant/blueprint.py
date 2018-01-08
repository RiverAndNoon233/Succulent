from plant.views.duoduo.main import main
from plant.views.mine.login import login
from plant.views.mine.register import regist
from plant.views.mine.change import change

#蓝本配置
DEFAULT_BLUEPRINT = (
    (main, ''),
    (login, '/user'),
    (regist, '/user'),
    (change, '/user'),

)

#封装函数，完成蓝本注册
def config_blueprint(app):
    for blueprint,prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint,url_prefix=prefix)