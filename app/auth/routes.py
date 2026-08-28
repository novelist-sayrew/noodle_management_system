from flask import render_template,redirect,url_for,flash,request,session
from flask_login import login_user,logout_user,login_required
from app.auth import bp
from app import db
from app.models import User,PasswordResetToken
from app.forms import RegistrationForm,LoginForm,OTPForm,ResetPasswordForm
from app.utils import send_email
from datetime import datetime,timedelta,timezone
from werkzeug.security import generate_password_hash
import secrets

@bp.route("/register",methods=["GET","POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(
            username = form.username.data,
            email = form.email.data
            )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("登録が完了しました。ログインしてください")
        return redirect(url_for("auth.login"))
    return render_template("auth/register.html",form=form)

@bp.route("/login",methods=["GET","POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user,remember=form.remember_me.data)
            next_page = request.args.get("next") or url_for("todo.index")
            return redirect(next_page)
        flash("ユーザー名またはパスワードが違います。")
    return render_template("auth/login.html",form=form)

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@bp.route("/forgot_password",methods=["GET","POST"])
def forgot_password():
    if request.method == "GET":
        return render_template("auth/forgot_password.html")

    email = request.form.get("email")
    user = User.query.filter_by(email=email).first()

    if not user:
        flash("メールアドレスが存在しません。")
        return redirect(url_for("auth.forgot_password"))

    token = secrets.token_urlsafe(32)
    expires_at = datetime.now(timezone.utc) + timedelta(hours=1)

    record = PasswordResetToken(
        email=email,
        token=token,
        expires_at=expires_at
    )

    db.session.add(record)
    db.session.commit()

    reset_url = url_for("auth.verify_token",token=token,_external=True)

    send_email(
        to_email=email,
        subject="パスワード再設定",
        body=f"以下のURLにアクセスして、パスワードの再設定をしてください。\n{reset_url}\n有効期限は1時間です。"
    )

    flash("パスワード再設定用のURLをメールで送信しました。")
    return redirect(url_for("auth.login"))

@bp.route("/reset_password",methods=["GET","POST"])
def reset_password():
    form = ResetPasswordForm()

    email = session.get("reset_email")

    if not email:
        flash("メールアドレス情報がありません。もう一度やり直してください。")
        return redirect(url_for("auth.forgot_password"))

    user = User.query.filter_by(email=email).first()

    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()

        session.pop("reset_email",None)

        flash("パスワードを変更しました。ログインしてください。")
        return redirect(url_for("auth.login"))

    return render_template("auth/reset_password.html",form=form)

@bp.route("/reset_password/<token>",methods=["GET"])
def verify_token(token):
    record = PasswordResetToken.query.filter_by(token=token,used=False).first()

    if not record:
        return "無効なURLです。"

    now = datetime.now(timezone.utc).replace(tzinfo=None)

    if record.expires_at < now:
        return "URLの有効期限が切れています。"

    record.used = True
    db.session.commit()

    session["reset_email"] = record.email

    return redirect(url_for("auth.reset_password"))

