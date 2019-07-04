#!/user/bin/env python
#coding=utf-8

# @project : rearend
# @author  : kalifun
# @file   : database.py
# @ide    : PyCharm
# @time   : 2019/7/2 11:41
from flask_script import Command
from one.model.models import db,User

class init_db(Command):
    def run(self):
        db.create_all()
        username = 'admin'
        password = 'admin'
        user = User(username=username,password=password)
        user.add()
        print("--------初始化完成---------")

class drop_db(Command):
    def run(self):
        db.drop_all()
        print("--------清除数据库完成---------")