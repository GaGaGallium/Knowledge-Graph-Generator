# 路由
from flask import Flask, jsonify, render_template, request, redirect, url_for, session

app = Flask(__name__)

DIALCT = "mysql"  # 数据库类型
DRIVER = "pymysql"  # 数据库驱动
USERNAME = "root"  # 数据库用户名
PASSWORD = "Gallium31"  # 数据库密码
HOST = "127.0.0.1"  # 服务器IP地址
PORT = "3306"  # 端口号，默认3306
DATABASE = "XXAQ"  # 数据库名
DB_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALCT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['UPLOAD_FOLDER'] = 'app/static/uploads'

from app.route.register import register
from app.route.login import login
from app.route.extraction import extraction
from app.route.generate import generate

@app.route('/', methods=["GET","POST"])
def mainpage():
    try:
        session["UserName"]
        return render_template('主页.html')
    except:
        return redirect('/注册')