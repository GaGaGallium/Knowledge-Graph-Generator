# 不是最终功能
from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from app.router import app
from app.models.ER import ER
import pandas as pd
import os

types = [
    '人物','作品','组织机构','物体','其他角色',
    '文化','生物','品牌','场所','世界地区',
    '饮食','药物','术语','疾病损伤','宇宙',
    '事件','时间'
]

def get_text(para, path):
    if path and para:
        return "别太着急哦，请只通过一种方式上传吧。"
    if path:
        file = open(path, 'r', encoding="utf-8")
        text = file.readlines()
    if para:
        text = para
    return text

@app.route('/抽取', methods=["GET", "POST"])
def extraction():
    if request.method == "GET":
        return render_template('抽取.html',types=types,render="False")
    else:
        file = request.files.get('file')
        path = os.path.join(app.config['UPLOAD_FOLDER'], '文本.txt')
        file.save(path)
        text = get_text(request.form.get('para'), path)
        r_option = request.form.get("radio")
        e_option = request.form.getlist("checkbox")
        er = ER(text, e_option, r_option)
        er.to_csv(f"{os.path.join(app.config['UPLOAD_FOLDER'], '抽取结果.csv')}")
        er.to_html(f"{os.path.join(app.config['UPLOAD_FOLDER'], '抽取结果.html')}")
        return render_template('抽取.html',types=types,render="True")