from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data1.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

db.create_all()

@app.route("/")
def index():
    return render_template("test.html")

if __name__ == "__main__":
    app.run(debug=True)

