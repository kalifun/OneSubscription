#!/user/bin/env python
#coding=utf-8

# @project : rearend
# @author  : kalifun
# @file   : run.py
# @ide    : PyCharm
# @time   : 2019/7/3 19:18
import os
from one.App.createapp import CreateApp
from one.utils.todos import registtodos
application = CreateApp()

if __name__ == '__main__':
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        registtodos()
    application.run()