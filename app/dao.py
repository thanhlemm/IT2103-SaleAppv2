"""Dùng để truy cập dữ liệu"""

from app.models import Category, Product


def load_categories():
    return Category.query.all()


def load_products(kw):
    # products = [{
    #     "id": 1,
    #     "name": "iPhone 15 Pro Max",
    #     "price": 20000000,
    #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690461425/bqjr27d0xjx4u78ghp3s.jpg"
    # }, {
    #     "id": 2,
    #     "name": "iPhone 15 Pro Max",
    #     "price": 20000000,
    #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690461425/bqjr27d0xjx4u78ghp3s.jpg"
    # }, {
    #     "id": 1,
    #     "name": "iPhone 15 Pro Max",
    #     "price": 20000000,
    #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690461425/bqjr27d0xjx4u78ghp3s.jpg"
    # }, {
    #     "id": 1,
    #     "name": "iPad Pro 2022",
    #     "price": 20000000,
    #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690461425/bqjr27d0xjx4u78ghp3s.jpg"
    # }, {
    #     "id": 1,
    #     "name": "iPhone 15 Pro Max",
    #     "price": 20000000,
    #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690461425/bqjr27d0xjx4u78ghp3s.jpg"
    # }]
    #
    # if kw:
    #     products = [p for p in products if p['name'].find(kw) >= 0]
    #
    # return products
    products = Product.query
    if kw:
        products = products.filter(Product.name.contains(kw))

    return products.all()
