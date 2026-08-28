from app import db,login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime,timedelta,timezone

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,nullable=False,)
    email = db.Column(db.String(255),unique=True,nullable=False)
    password_hash = db.Column(db.String(128),nullable=False)

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

@login.user_loader
def load_user(user_id):
    return db.session.get(User,int(user_id)) #セッションからuser_idを呼び出し、それを元に、再ログインされた時にログイン情報を復元する。

class Todo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    expiry_date = db.Column(db.Date)
    title = db.Column(db.String(120))

class PasswordResetToken(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),nullable=False)
    token = db.Column(db.String(255),unique=True,nullable=False)
    expires_at = db.Column(db.DateTime,nullable=False)
    used = db.Column(db.Boolean,default=False)