#!/user/bin/env python
#coding=utf-8

# @project : rearend
# @author  : kalifun
# @file   : models.py
# @ide    : PyCharm
# @time   : 2019/7/2 11:26
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
db = SQLAlchemy()

class User(UserMixin,db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    pwd_hash = db.Column(db.String(128))
    createtime = db.Column(db.DateTime,default=datetime.now)

    def __init__(self,username,password):
        self.name = username
        self.generate_password(password=password)

    def generate_password(self,password):
        self.pwd_hash = generate_password_hash(password=password)

    def check_password(self,password):
        return check_password_hash(self.pwd_hash,password=password)

    def add(self):
        db.session.add(self)
        db.session.commit()

class Subscription(db.Model):
    __tablename__ = 'email'
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    emailadd = db.Column(db.String(120), unique=True)
    addtime = db.Column(db.DateTime,default=datetime.now)
    locked = db.Column(db.BOOLEAN,default=False)

    def __init__(self,emailadd):
        self.emailadd = emailadd

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict

    def add(self):
        db.session.add(self)
        db.session.commit()

    def lock(self,idbool):
        self.locked = idbool
        db.session.commit()

    def delmail(self):
        db.session.delete(self)
        db.session.commit()
