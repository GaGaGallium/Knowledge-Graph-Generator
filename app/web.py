# import imp
# import os
# from wsgiref.simple_server import make_server

# def application(unicorvn,start_response):
#     start_response('200 OK',[('Content-Type','text/html')])
#     return [b'<h1>hello world, hello 403, ga']

# httpd = make_server('0.0.0.0',8000,application)

# httpd.serve_forever()


import os
from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)

@app.route('/')
def home():
    if "username" in session:
        return f"Already login as {session['username']}"
    else:
        return redirect(url_for(".login"))

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template('hello.html')
    else:
        name = request.form.get("name")
        password = request.form.get("password")
        session["username"] = name
        return f"{name},{password}"

@app.route('/username/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post):
    return 'Post %d' % post

@app.route('/showname')
def show_name():
    name = request.args.get("name")
    return 'Name %s' % name

