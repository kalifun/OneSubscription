#!/user/bin/env python
#coding=utf-8

# @project : rearend
# @author  : kalifun
# @file   : api.py
# @ide    : PyCharm
# @time   : 2019/7/2 12:35

from flask import Blueprint,request,abort,jsonify,render_template,redirect,url_for,flash
from one.model.models import Subscription,User
from flask_login import login_user,logout_user,login_required,LoginManager
from one.mail.regist.hello import sedmail

api = Blueprint('api',__name__,template_folder='template',static_folder='static')
login_manager = LoginManager()

@api.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        email = request.form.get("email")
        if not all([email]):
            abort(401)
        emailinfo = Subscription.query.filter_by(emailadd=email).first()
        if emailinfo:
            # return jsonify({"message":"此邮箱已订阅"})
            flash("此邮箱已订阅","ok")
            return redirect(url_for('api.index'))
        else:
            sedmail(email)
            tryadd = Subscription(emailadd=email)
            tryadd.add()
            flash("订阅成功", "ok")
            return redirect(url_for('api.index'))
            # return jsonify({"success":"订阅成功"})

@api.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        if not all([username,password]):
            return render_template('login.html',error_msg='参数不完整')
        user = User.query.filter(User.name == username).first()
        if user:
            if user.check_password(password=password):
                login_user(user=user)
                return redirect(url_for('api.list'))
            else:
                return render_template('login.html',error_msg='用户密码错误')
        else:
            return render_template('login.html',error_msg='用户不存在')

@api.route('/list',methods=['GET'])
@login_required
def list():
    if request.method == 'GET':
        list = Subscription.query.all()
        result = []
        for newlist in list:
            result.append(newlist.to_json())
        # return jsonify({"message":result})
        return render_template('list.html',result=result)

@api.route('/locked',methods=['GET'])
@login_required
def locked():
    if request.method == 'GET':
        listadd = request.args.get("listadd")
        lock = Subscription.query.filter(Subscription.emailadd == listadd).first()
        if lock:
            nowlock = bool(1- (lock.locked))
            lock.lock(nowlock)
            return redirect(url_for('api.list'))

@api.route('/delete',methods=['GET'])
@login_required
def delete():
    if request.method == 'GET':
        listadd = request.args.get("listadd")
        dele = Subscription.query.filter(Subscription.emailadd == listadd).first()
        if dele:
            dele.delmail()
            return redirect(url_for('api.list'))

@api.route('/addmail',methods=['GET','POST'])
def addmail():
    if request.method == 'GET':
        return redirect(url_for('api.index'))


@api.route('/logout',methods=['GET'])
def logout():
    if request.method == 'GET':
        logout_user()
        return redirect(url_for('api.login'))

# @api.route('/allmail',methods=['GET'])
# def allmail():
#     if request.method == 'GET':
#         list = Subscription.query.with_entities(Subscription.emailadd).all()
#         result = []
#         for newlist in list:
#             result.append(newlist[0])
#         return  jsonify({"xxx":result})

@login_manager.user_loader
def load_user(user_id):
    curr_user = User.query.get(user_id)
    if curr_user is not None:
            curr_user.id = user_id
            return curr_user