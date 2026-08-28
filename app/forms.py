from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,PasswordField,BooleanField,DateField,SubmitField
from wtforms.validators import DataRequired,Length,EqualTo,ValidationError,Email
from app.models import User

class RegistrationForm(FlaskForm):
    username = StringField("ユーザー名",validators=[
        DataRequired(),
        Length(min=1,max=64)
    ])
    email = EmailField("Eメールアドレス",validators=[
        DataRequired(),Email()
    ])
    password = PasswordField("パスワード",validators=[
        DataRequired(),
        Length(min=6)
    ])
    password2 = PasswordField("パスワード(確認)",validators=[
        DataRequired(),
        EqualTo("password")
    ])
    submit = SubmitField("登録")

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("このユーザー名は既に使用されています。")

class LoginForm(FlaskForm):
    username = StringField("ユーザー名",validators=[DataRequired()])
    password = PasswordField("パスワード",validators=[DataRequired()])
    remember_me = BooleanField("ログイン状態を保持する")
    submit = SubmitField("ログイン")

class TodoForm(FlaskForm):
    expiry_date = DateField("賞味期限",format="%Y-%m-%d",validators=[
        DataRequired()
    ])
    title = StringField("商品名",validators=[
        DataRequired(),
        Length(max=120)
    ])
    submit = SubmitField("保存")

class OTPForm(FlaskForm):
    otp = StringField("ワンタイムパスワード",validators=[
        DataRequired()
    ])
    submit = SubmitField("送信")

class ResetPasswordForm(FlaskForm):
    password = PasswordField("新しいパスワード",validators=[
        DataRequired()
    ])
    confirm = PasswordField("新しいパスワード(確認)",validators=[
        DataRequired(),
        EqualTo("password")
    ])
    submit = SubmitField("変更する")
