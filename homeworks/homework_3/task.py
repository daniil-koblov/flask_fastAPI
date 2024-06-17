from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User
from forms import RegisterForm

app = Flask(__name__)

# указываем адрес базы данных, а также ее тип
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db.init_app(app)

# настраиваем секретный ключ
app.config["SECRET_KEY"] = (
    "aff4028c6c00ebb18a75309c87787c6b488eb83149bb1af1c427c85715c022b9"
)
csrf = CSRFProtect(app)


# перед первым запуском приложения необходимо создать базу данных
# (в терминале прописываем команду: flask init-db)
@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.route("/")
@app.route("/index/")
def index():
    return render_template("index.html", title="Главная страница")


@app.route("/registration/", methods=["GET", "POST"])
def registration():
    form = RegisterForm()
    context = {"title": "Страница регистрации", "form": form}
    if request.method == "POST" and form.validate():
        # получаем данные из формы
        name = form.name.data
        surname = form.surname.data
        mail = form.mail.data

        # при получении пароля сразу шифруем его
        secret_password = generate_password_hash(form.password.data)

        # Проверяем есть ли в БД такой мэйл
        user = User.query.filter_by(mail=mail).first()
        if user:
            flash(
                "Пользователь с такой электронной почтой уже зарегистрирован!",
                "danger"
            )
            return redirect(url_for("registration"))

        # добавляем пользователя в БД
        new_user = User(name=name, surname=surname, mail=mail,
                        password=secret_password)
        db.session.add(new_user)
        db.session.commit()

        flash(f"Здравствуйте {name} {surname}!Вы успешно зарегистрированы!!!",
              "success")
        return redirect(url_for("index"))

    return render_template("registration.html", **context)


if __name__ == "__main__":
    app.run(debug=True)