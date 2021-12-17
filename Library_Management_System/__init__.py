"""
The flask application package.
Importing DB config from config.py and intializing Application
"""

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")
db = SQLAlchemy(app)
login_manager = LoginManager(app)
migrate = Migrate(app, db)
