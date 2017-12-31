import os

base_dir = os.path.abspath(os.path.dirname(__file__))

#通用配置
class Config:
    #密钥
    SECRET_KEY = os.environ.get('SECRET_KEY') or '12345'
    # 数据库
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 邮件发送
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.163.com'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'm2809695868@163.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'shao08251400'

    UPLOADED_PHOTOS_DEST = os.path.join(base_dir,'static/icon')
    MAX_CONTENT_LENGTH = 2*1024*1024
    #额外的初始化操作，即使什么内容都没有写，也是有意义的
    @staticmethod
    def init_app(app):
        pass

#开发环境
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir,'succulent_dev.sqlite')
#测试环境
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir,'succulent_test.sqlite')
#生成环境
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir,'succulent.sqlite')

#配置字典
config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'production' : ProductionConfig,
    'default' : DevelopmentConfig
}