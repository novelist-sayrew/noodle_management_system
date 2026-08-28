from flask import Flask,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
import config

db = SQLAlchemy()
login = LoginManager()
mail = Mail()

login.login_view = "auth.login"

login.login_message = "ログイン、または新規登録を行ってください。"

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = config.SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = config.DATABASE_URL

    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = 587
    app.config["MAIL_USE_TLS"] = True
    app.config["MAIL_USERNAME"] = config.MAIL_USERNAME
    app.config["MAIL_PASSWORD"] = config.MAIL_PASSWORD
    app.config["MAIL_DEFAULT_SENDER"] = config.MAIL_USERNAME

    mail.init_app(app)

    db.init_app(app)
    login.init_app(app)

    with app.app_context():
        from app.auth import bp as auth_bp
        from app.todo import bp as todo_bp

        app.register_blueprint(auth_bp,url_prefix="/auth")
        app.register_blueprint(todo_bp,url_prefix="/todo")

        db.create_all()

        @app.route("/")
        def root():
            return redirect("/todo/")
    return app




