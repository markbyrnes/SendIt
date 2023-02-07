from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment
from flask_bootstrap import Bootstrap
import logging
from logging.handlers import RotatingFileHandler
import os


app = Flask(__name__)
app.config.from_object(Config) #defines config file

db = SQLAlchemy(app) #defines database
migrate = Migrate(app, db) #defines the migration engine from app to database

login = LoginManager(app)
login.login_view = 'login'

bootstrap = Bootstrap(app)
moment = Moment(app) 

#error logging for production mode
if not app.debug:
    if not os.path.exists('logs'):  #creates log file and directory
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/sendit.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Sendit startup')
from app import routes, models, errors #do not move to top, prevents circular import error
