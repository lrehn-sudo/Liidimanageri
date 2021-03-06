from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from flask_cors import CORS
from config import config
import logging

logging.getLogger('flask_cors').level = logging.DEBUG
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    # CORS(app)
    # app.config["SQLALCHEMY_ECHO"] = True
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    # print(config[config_name].SQLALCHEMY_DATABASE_URI)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    username=app.config['DB_USERNAME']
    password=app.config['DB_PASSWORD']
    print("DB_USERNAME:"+username+",DB_PASSWORD:"+password)
    return app
