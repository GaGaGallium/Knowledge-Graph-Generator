from ..router import app
from .model import db
    
class User(db.Model):
    # 定义表名
    __tablename__ = 'Login'
    # 定义字段
    # primary_key=True 设置为主键
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)    #autoincrement自增可以自动输入不重复的id
    UserName = db.Column(db.String(255))
    Password = db.Column(db.String(255))
    Email = db.Column(db.String(255))

    # 构造函数
    def __init__(self, UserName, Password, Email) -> None:
        self.UserName = UserName
        self.Password = Password
        self.Email = Email

    # 打印形式
    def __str__(self):
        return "ID:%s, name:%s, password:%s, email:%s" % (
            str(self.ID), self.UserName, self.Password, self.Email)
