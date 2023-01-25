# 入口启动文件
from app.router import app
import os


app.secret_key = os.urandom(24)
app.run(host='0.0.0.0',debug=True)
