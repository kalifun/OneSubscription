#!/user/bin/env python
#coding=utf-8

# @project : rearend
# @author  : kalifun
# @file   : createapp.py
# @ide    : PyCharm
# @time   : 2019/7/2 11:19

from flask import Flask
from one.config.config import Config
from one.model.models import db
from one.apibuleprint.api import api
from one.apibuleprint.api import login_manager
from one.mail.regist.hello import mail
from one.utils.todos import scheduler

def CreateApp():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(blueprint=api,url_prefix='/one')
    login_manager.init_app(app=app)
    login_manager.login_view = 'api.login'
    login_manager.login_message = 'Please login'
    login_manager.session_protection = 'onemail'

    scheduler.init_app(app=app)
    scheduler.start()
    mail.init_app(app=app)
    db.init_app(app=app)
    return app