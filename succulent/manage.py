import os

from plant import create_app
from flask_script import Manager
from flask_migrate import MigrateCommand

#获取配置
config_name = os.environ.get('FLASK_CONFIG') or 'default'
#创建Flask实例
app = create_app(config_name)

#创建命令行启动控制对象
manager = Manager(app)

manager.add_command('db',MigrateCommand)

#启动项目
if __name__ == '__main__':
    manager.run()