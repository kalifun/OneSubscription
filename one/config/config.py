#!/user/bin/env python
#coding=utf-8

# @project : rearend
# @author  : kalifun
# @file   : config.py
# @ide    : PyCharm
# @time   : 2019/7/2 11:22

class Config():
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://用户:密码@localhost:数据库端口/数据库'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'Onemail'
    # 电子邮件服务器的主机名或IP地址
    MAIL_SERVER = 'smtp.163.com'
    # 电子邮件服务器的端口
    MAIL_PORT = 25
    # 启用传输层安全
    MAIL_USE_TLS = True
    # 你的邮件账户用户名

    # 阿里云对25端口限制，如有被限制的请注释上面两行
    # MAIL_PORT = 465
    # MAIL_USE_SSL = False

    # 邮件名称
    MAIL_USERNAME = ''
    # 邮件账户的密码,这个密码是指的授权码!授权码!授权码!
    MAIL_PASSWORD = ''

    #定时任务接口
    SCHEDULER_API_ENABLED = True

    # 公开服务上请修改为False
    DEBUG = True