from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
from app import app, db
from app.models import Category, Product


admin = Admin(app=app, name='QUẢN TRỊ BÁN HÀNG', template_mode='bootstrap4')
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Product, db.session))