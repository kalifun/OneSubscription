# One 一个

## 前言

> 此程序是利用爬虫将One主页的信息拉取，定时以邮件形式发送。

**环境：**

- 框架：Flask
- Python： 3+

## 部署步骤

### Python环境

**此步骤省略**

### 安装虚拟环境

```
pip3 install virtualenv
```

### 创建虚拟环境

```
# 进入到你想创建的目录
virtualenv venv
```

**目录下就有一个venv 文件夹了。**

### 激活虚拟环境

```
source venv/bin/activate
```

### 安装模块

```
pip install -r requirements.txt
```

### 修改程序

**one/config/config.py**

```
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://用户名:密码.@localhost:端口/数据库'
# 电子邮件服务器的主机名或IP地址
MAIL_SERVER = 'smtp.163.com'
# 电子邮件服务器的端口
MAIL_PORT = 25
# 启用传输层安全
MAIL_USE_TLS = True

#阿里云对25端口限制，如有被限制的请注释上面两行
# MAIL_PORT = 465
# MAIL_USE_SSL = True

# 你的邮件账户用户名
MAIL_USERNAME = ''
# 邮件账户的密码,这个密码是指的授权码!授权码!授权码!
MAIL_PASSWORD = ''

# 公开服务上请修改为False
DEBUG = True
```

**one/utils/database.py**

```
# 后台登录的用户名密码
username = 'admin'
password = 'admin'
```



### 创建数据库

```
省略
```

### 程序初始化

```
python manage.py init
```

### 安装gunicorn

```
pip install gunicorn
```

### 测试启动服务

```
gunicorn -w 4 -b 127.0.0.1:8000 run:application

curl http://127.0.0.1:8000/one/index
```

### 配置nginx

```
server {
        listen 80;
        server_name 域名;

        location / {
                proxy_pass http://127.0.0.1:8000/one/;
                proxy_set_header Host $host;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
}
```

### 安装supervisor

```
$ pip install supervisor
$ echo_supervisord_conf > supervisor.conf   # 生成 supervisor 默认配置文件
$ vim supervisor.conf                       # 修改 supervisor 配置文件，添加 gunicorn 进程管理
```

```
[program:oneflask]
command=/home/wwwroot/oneflask -w 4 -b 0.0.0.0:8000 run:application    ;supervisor启动命令         
directory=/home/www/blog                                                 ; 项目的文件夹路径
startsecs=0                                                               ; 启动时间
stopwaitsecs=0                                                            ; 终止等待时间
autostart=false                                                           ; 是否自动启动
autorestart=false                                                         ; 是否自动重启
stdout_logfile=/home/wwwroot/oneflask/logs/gunicorn.log                            ; log 日志
stderr_logfile=/home/wwwroot/oneflask/logs/gunicorn.err                            ; 错误日志

```

### 使用 supervsior 启动 gunicorn

```
$ sudo supervisord -c supervisor.conf  
$ sudo supervisorctl start oneflask
```

## 问题

**经过测试如果使用gunicorn启动程序，定时任务并不能执行。我也不知道是不是因为定时任务我重新注册了一个flask的原因。**

```
python manage.py runserver
python run.py
这些都是正常工作的。
```

## 效果

![](https://image.kalifun.top/upload/1907/6765f8b4e6f6ff46.png)

**后台比较简陋我就不展现出来了。**

## 接口

- [x] 后台登录
- [x] 后台登出
- [x] 删除邮箱
- [x] ~~锁定邮件(因为和删除邮件相同功能)~~
- [x] 添加邮件

## 模块

- **ORM： Flask-SQLAlchemy**
- **认证：Flask-Login**
- **插件：Flask-Script（初始化数据，删除数据等）**
- **定时任务：Flask-Apscheduler**
- **邮箱服务：Flask-Mail**
- **密码：Hash**

## 鸣谢

**[[ONE - 一个]](http://www.wufazhuce.com/)**

