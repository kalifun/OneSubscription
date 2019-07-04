#!/user/bin/env python
#coding=utf-8

# @project : rearend
# @author  : kalifun
# @file   : todos.py
# @ide    : PyCharm
# @time   : 2019/7/3 15:23
from flask_apscheduler import APScheduler
from flask import current_app,Flask
from one.model.models import Subscription
from one.config.config import Config
from one.model.models import db
from one.mail.regist.hello import everydaysed
from one.utils.spiderone import OneSpider
from one.mail.regist.hello import mail
scheduler = APScheduler()

# def Subscribetomail():
#     msginfo = OneSpider().Processfile()
#
#     list = Subscription.query.with_entities(Subscription.emailadd).all()
#     print(msginfo)
#     print(list)
#     result = []
#     for newlist in list:
#         result.append(newlist[0])
    # everydaysed(msginfo=msginfo,mailist=result)
def Subscribetomail():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app=app)
    mail.init_app(app=app)
    with app.app_context():
        print(current_app.name)
        msginfo = OneSpider().Processfile()
        list = Subscription.query.with_entities(Subscription.emailadd).all()
        result = []
        for newlist in list:
            result.append(newlist[0])
        print(result)
        everydaysed(msginfo=msginfo,mailist=result)


def registtodos():
    job = {
        'id': 'send mail every day',
        'func': 'Subscribetomail'
    }
    # result = scheduler.add_job(func=__name__+':'+job['func'],id=job['id'],trigger='cron', hour='22',minute='30')
    result = scheduler.add_job(func=__name__ + ':' + job['func'], id=job['id'], trigger='cron', hour= '11',minute='02')
    print(result)
