from flask import Flask
from sqlalchemy import create_engine, Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class conn():
    id = db.Column(db.Integer, primary_key=True)
    # engine = create_engine('sqlite:///database.sqlite3')
    # @classmethod
    # def estalish(cls):
    #     return cls.engine
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'

# engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
# print([dict(e) for e in engine.connect().execute('SELECT * FROM labs;')])
# print(engine.connect().execute("SELECT * FROM labs;").fetchall())
# print(engine.connect().execute("SELECT * FROM labs;").keys())
# print(engine.connect().execute("SELECT * FROM labs;").first()['name'])