from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from app.router import app
from app.models.model import db
from app.models.users import User
from app.models.md5 import pwd_md5
from app.models.warning import Warning

@app.route('/注册', methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template('注册.html')
    else:
        name = request.form.get("name")
        if User.query.filter_by(UserName=name).first() is not None:
            return render_template('error.html', warning=Warning("register","用户已存在！"))
        else:  
            password = pwd_md5(request.form.get("password"))
            email = request.form.get("email")
            user = User(name,password,email)
            db.session.add(user)
            db.session.commit()
            return render_template('register_success.html', id=user.ID, username=user.UserName, password=user.Password, email=user.Email)
        
