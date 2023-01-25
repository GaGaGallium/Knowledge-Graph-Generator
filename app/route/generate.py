from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from app.router import app
from pyecharts.charts import Graph
from pyecharts import options as opts
import os
import pandas as pd

@app.route('/生成', methods=["GET", "POST"])
def generate():
    if request.method == "GET":
        return render_template('生成.html',render="False")
    else:
        file = request.files.get('file')
        path = os.path.join(app.config['UPLOAD_FOLDER'], '数据.csv')
        file.save(path)
        df = pd.read_csv(path)
        nodes = df[0:df[df["Unnamed: 0"]==0].index[1]]
        links = df[df[df["Unnamed: 0"]==0].index[1]:]
        node_size = request.form.get('node_size')
        if node_size == "":
            node_size = 1
        else:
            node_size = float(node_size)
        link_size = request.form.get('link_size')
        if link_size == "":
            link_size = 1
        else:
            link_size = float(link_size)
        nodes = [{"name": i[1]['entity'], "symbolSize": i[1]['mark']*node_size} for i in nodes.iterrows()]
        links = [{"source": i[1]['head'], "target": i[1]['tail'], "value": i[1]['mark'], "symbolSize": link_size} for i in links.iterrows()]
        c = (
            Graph()
            .add(
                "",nodes,links,
                repulsion=4000,
                edge_label=opts.LabelOpts(is_show=True, position="middle"),
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Graph-GraphNode-GraphLink-WithEdgeLabel")
            )
            .render(f"{os.path.join(app.config['UPLOAD_FOLDER'], '生成结果.html')}")
        )
        return render_template('生成.html',render="True")