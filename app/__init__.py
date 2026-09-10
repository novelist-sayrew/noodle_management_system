from flask import Flask,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
import config
import os

db = SQLAlchemy()
login = LoginManager()
mail = Mail()

login.login_view = "auth.login"
login.login_message = "ログイン、または新規登録を行ってください。"

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = 587
    app.config["MAIL_USE_TLS"] = True
    app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
    app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
    app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

    mail.init_app(app)
    db.init_app(app)
    login.init_app(app)

    from app.models import User,PasswordResetToken
    from app.scheduler import init_scheduler

    init_scheduler(app)

    with app.app_context():
        from app.auth import bp as auth_bp
        from app.noodle import bp as noodle_bp

        app.register_blueprint(auth_bp,url_prefix="/auth")
        app.register_blueprint(noodle_bp,url_prefix="/noodle")

        db.create_all()

        @app.route("/")
        def root():
            return redirect("/noodle/")
    return app

