from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello world"


@app.route("/about/")
def about():
    return "About"


@app.route("/contact/")
def contact():
    return "Contact"


@app.route("/<int:num1>/<int:num2>/")
def sum_number(num1, num2):
    return f'Сумма переданных чисел {num1} и {num2} равна {num1 + num2}.'


@app.route("/get-length-row/<string:row>/")
def get_lenght_row(row):
    return str(len(row))


@app.route("/get-html/")
def get_html():
    return """
    
    <h1>Hello!</h1>
    """


@app.route("/info-about-students/")
def get_info():
    students = [
        {"name": "Alex", "surname": "Black", "age": "19", "rating": "4.7"},
        {"name": "Mike", "surname": "Donowan", "age": "18", "rating": "4.3"},
        {"name": "Luke", "surname": "Skywalker", "age": "20", "rating": "5.0"}
    ]
    return render_template("tmp.html", students=students)


@app.route("/news/")
def news():
    news = [
        {"title": "title", "date": "01.01.2024", "description": "some news"},
        {"title": "title", "date": "01.01.2024", "description": "some news"},
        {"title": "title", "date": "01.01.2024", "description": "some news"},
        {"title": "title", "date": "01.01.2024", "description": "some news"}
    ]
    return render_template("news.html", news=news)


if __name__ == '__main__':
    app.run(debug=True)
