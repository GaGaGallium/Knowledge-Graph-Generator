import sys
from flask_sqlalchemy import SQLAlchemy
from ..router import app

db = SQLAlchemy(app)