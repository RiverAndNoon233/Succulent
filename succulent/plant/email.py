from plant.extensions import mail
from flask import current_app, render_template
from flask_mail import Message
from threading import Thread


def async_send_mail(app, msg):
    # 发送邮件必须在程序上下文中，新的线程中需要手动创建
    with app.app_context():
        mail.send(msg)


# 封装函数发送邮件
def send_mail(to, subject, template, **kwargs):
    # 根据代理对象current_app，找到实例化的app对象
    app = current_app._get_current_object()
    msg = Message(subject=subject, recipients=[to],
                  sender=app.config['MAIL_USERNAME'])
    msg.html = render_template(template + '.html', **kwargs)
    msg.body = render_template(template + '.txt', **kwargs)
    # 创建线程
    thr = Thread(target=async_send_mail, args=[app, msg])
    # 启动线程
    thr.start()
    return thr
