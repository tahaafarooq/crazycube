from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login = LoginManager()


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    msisdn = db.Column(db.String, primary_key=True)
    balance = db.Column(db.Integer)
    password = db.Column(db.String(80))


class Messages(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    msisdn = db.Column(db.String(80))
    message = db.Column(db.String())


class Withdraws(db.Model):
    __tablename__ = 'withdraws'
    id = db.Column(db.Integer, primary_key=True)
    msisdn = db.Column(db.String())
    amount = db.Column(db.Integer)
    message = db.Column(db.String())
