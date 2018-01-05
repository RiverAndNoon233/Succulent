from flask import Flask, render_template
from plant.config import config
from plant.extensions import config_extensions
from plant.blueprint import config_blueprint
# from plant.models import User
#封装一个方法，专门用于创建Flask实例
def create_app(config_name):
    #创建应用实例
    app = Flask(__name__)
    #初始化配置
    app.config.from_object(config.get(config_name) or config.get('default'))
    #调用初始化函数
    config[config_name].init_app(app)
    #配置扩展
    config_extensions(app)
    #配置蓝本
    config_blueprint(app)
    #错误页面定制
    config_errorhandle(app)
    #返回应用实例
    return app

def config_errorhandle(app):
    pass
#     #如果在蓝本定制，只针对本蓝本有效
#     #使用@app.errorhandler可以在全局生效
#     @app.errorhandler(404)
#     def page_not_found(e):
#         return render_template('404.html')