from flask import render_template, request
import dao
from app import app, login


@app.route('/')
def index():
    kw = request.args.get('kw')
    cates = dao.load_categories()
    products = dao.load_products(kw)
    return render_template('index.html', categories=cates, products=products)


@app.route('/admin/login', method=['post'])
def process_admin_login():
    request.form.get('username')
    request.form.get('password')

@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    from app import admin

    app.run(debug=True, port=5001)
