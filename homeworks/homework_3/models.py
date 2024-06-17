from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    mail = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)

    def __str__(self) -> str:
        return f'Имя: {self.name}, Фамилия: {self.surname}, Email: {self.mail}'