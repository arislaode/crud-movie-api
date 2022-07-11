
from app import app 
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()

url_db = os.getenv("URL_DB")
username_db = os.getenv("USERNAME_DB")
password_db = os.getenv("PASSWORD_DB")
name_db =os.getenv("NAME_DB")
secret_key = os.getenv("SECRET_KEY")

app.config['SECRET_KEY'] = secret_key
app.config["SQLALCHEMY_DATABASE_URI"]=f'postgresql://{username_db}:{password_db}@{url_db}/{name_db}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    public_id = db.Column(db.String(50), unique = True)
    username = db.Column(db.String(100))
    fullname = db.Column(db.String(70), unique = True)
    password = db.Column(db.String(150))

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    rating = db.Column(db.Float)
    image = db.Column(db.LargeBinary)
    owned = db.Column(db.String(30))