from plant.views.duoduo.main import main


#蓝本配置
DEFAULT_BLUEPRINT = (
    (main,''),

)

#封装函数，完成蓝本注册
def config_blueprint(app):
    for blueprint,prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint,url_prefix=prefix)