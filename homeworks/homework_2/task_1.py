from flask import (
    Flask,
    render_template,
    request,
    make_response,
    redirect,
    url_for,
)

app = Flask(__name__)
app.secret_key = "816b422c25127e8a51af86a65e2821b3c23bc6407baa64f37281382b503b204a"


@app.route("/")
@app.route("/index/")
def index():
    name = request.cookies.get("username")
    if name:
        context = {"name": name}
        response = make_response(render_template("index.html", **context))
        return response

    return redirect(url_for("login"))


@app.route("/login/", methods=["GET", "POST"])
def login():
    context = {"title": "Страница входа"}
    if request.method == "POST":
        name = request.form.get("name")
        mail = request.form.get("mail")
        context["name"] = name
        response = make_response(render_template("index.html", **context))
        response.set_cookie("username", name)
        response.set_cookie("usermail", mail)
        return response
    response = make_response(render_template("login.html"))
    response.delete_cookie("username")
    response.delete_cookie("usermail")
    return response
