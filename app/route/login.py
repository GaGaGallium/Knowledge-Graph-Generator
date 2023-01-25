from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from app.router import app
from app.models.model import db
from app.models.users import User
from app.models.md5 import pwd_md5
from app.models.warning import Warning

@app.route('/登录', methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template('登录.html')
    else:
        name = request.form.get("name")
        try:
            object = User.query.filter_by(UserName=name).first()
            password = pwd_md5(request.form.get("password"))
            if (password==object.Password):
                session["UserName"] = name
                return redirect("/")
            else:
                return render_template('error.html', warning=Warning("login","密码不正确！"))
        except:  
            return render_template('error.html', warning=Warning("login","用户不存在！"))