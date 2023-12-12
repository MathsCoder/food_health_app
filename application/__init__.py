import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from flask_login import LoginManager
from logging.handlers import RotatingFileHandler
from flask.logging import default_handler
import logging

basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()
db_migration = Migrate()
csrf_protection = CSRFProtect()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__, template_folder="templates")

    # Get flask config type
    flask_config = os.getenv("FLASK_CONFIG", default="config.DevelopmentConfig")
    app.config.from_object(flask_config)
    db.init_app(app)
    db_migration.init_app(app, db)
    csrf_protection.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "users.login"

    # Register blueprints
    from application.uploads.routes import upload_blueprint
    from application.users.routes import users_blueprint
    from application.main.routes import main_blueprint

    app.register_blueprint(upload_blueprint, url_prefix="/upload")
    app.register_blueprint(users_blueprint, url_prefix="/users")
    app.register_blueprint(main_blueprint)

    configure_logging(app)
    return app


def configure_logging(app):
    # Configure logging
    app.logger.removeHandler(default_handler)
    app.logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"
    )
    file_handler = RotatingFileHandler(
        "logs/food-health-app.log", maxBytes=10000, backupCount=10
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info("Flask app started")
