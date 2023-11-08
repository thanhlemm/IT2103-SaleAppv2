from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

# section là đối tượng mã hoá nên cần phải mã hoá qua secret key. Thêm, sửa, xoá kh bị lỗi

app.secret_key = '12lknr3lnfewl@#hskoq823kdgc72%%@!jasuh'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Abcd1234@localhost/saledbv2?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)
login = LoginManager(app=app)
