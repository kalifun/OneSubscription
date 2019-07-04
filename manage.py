#!/user/bin/env python
#coding=utf-8

# @project : rearend
# @author  : kalifun
# @file   : manage.py
# @ide    : PyCharm
# @time   : 2019/7/2 11:17
import os
from flask_script import Manager
from one.App.createapp import CreateApp
from one.utils.database import init_db,drop_db
from one.utils.todos import registtodos

app = CreateApp()
manage = Manager(app=app)

manage.add_command('init',init_db)
manage.add_command('drop',drop_db)

if __name__ == '__main__':
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        registtodos()
    manage.run()