from . import db, login_manager, bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=True)
    email = db.Column(db.String(40), unique=False, nullable=True)
    phone = db.Column(db.String(15), unique=False, nullable=True)
    subject = db.Column(db.Integer, unique=False, nullable=True)
    message = db.Column(db.Text, unique=False, nullable=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.password}')"

    def __init__(self, username, email, password, image_file='default.jpg'):
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.image_file = image_file

    def verify_password(self, pwd):
        return bcrypt.check_password_hash(self.password, pwd)
