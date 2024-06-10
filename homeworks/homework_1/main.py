from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    context = {"title": "Главная"}
    return render_template("index.html", **context)


@app.route("/faq/")
def faq():
    questions = [
        {
            "question": "Как сделать заказ?",
            "answer": "На сайте, позвонить нам или прийти в гости",
        },
        {
            "question": "Как забрать заказ?",
            "answer": "Приехать к нам или заказть доставку",
        },
        {
            "question": "Можно ли примерить?",
            "answer": "А кто вам откажет?",
        },
    ]
    context = {"title": "ЧАВо", "questions": questions}
    return render_template("faq.html", **context)


@app.route("/contacts/")
def contacts():
    context = {"title": "Контакты", }
    return render_template("contacts.html", **context)


@app.route("/clothes/")
def clothes():
    _clothes = [
        {
            "title": "Кофта",
            "price": "1000,00",
            "picture": "/static/clothes/image.jpg",
        },
        {
            "title": "Куртка",
            "price": "5500,00",
            "picture": "/static/clothes/image.jpg",
        },
        {
            "title": "Штаны",
            "price": "2300,00",
            "picture": "/static/clothes/image.jpg",
        },

    ]
    context = {"title": "Одежда", "clothes": _clothes}
    return render_template("clothes.html", **context)


@app.route("/shoes/")
def shoes():
    _shoes = [
        {
            "title": "Кроссовки",
            "price": "1500,00",
            "picture": "/static/shoes/image.jpg",
        },
        {
            "title": "Кеды",
            "price": "500,00",
            "picture": "/static/shoes/image.jpg",
        },
        {
            "title": "Тапки",
            "price": "300,00",
            "picture": "/static/shoes/image.jpg",
        },

    ]
    context = {"title": "Обувь", "shoes": _shoes}
    return render_template("shoes.html", **context)


@app.route("/hats/")
def hats():
    _hats = [
        {
            "title": "Шапка",
            "price": "1200,00",
            "picture": "/static/hats/image.jpg",
        },
        {
            "title": "Кепка",
            "price": "3500,00",
            "picture": "/static/hats/image.jpg",
        },
        {
            "title": "Бандана",
            "price": "1700,00",
            "picture": "/static/hats/image.jpg",
        },

    ]
    context = {"title": "Головные уборы", "hats": _hats}
    return render_template("hats.html", **context)


if __name__ == "__main__":
    app.run()