from flask import url_for
from ..router import app
    
class Warning():

    # 构造函数
    def __init__(self, link:str, message:str) -> None:
        self.link = url_for(link)
        self.message = message
        #self.memory = memory
