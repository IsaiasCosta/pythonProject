#definir o apap - criaçaõ do site


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] ="sqlite:///comunidade.bd"

database = SQLAlchemy(app)

from pythonrest import routes
