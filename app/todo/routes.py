from flask import render_template,redirect,url_for,flash,request
from flask_login import login_required,current_user
from app.todo import bp
from app import db
from app.models import Todo
from app.forms import TodoForm
from datetime import date,datetime,timedelta

@bp.route("/")
@login_required
def index():
    todos = Todo.query.order_by(Todo.expiry_date.asc()).all()
    today = date.today()

    for todo in todos:
        todo.remaining_days = (todo.expiry_date - today).days
    expired_items = Todo.query.filter(Todo.expiry_date < today).all()
    return render_template("todo/list.html",todos=todos,expired_items=expired_items)

@bp.route("/warning")
@login_required
def warning():
    today = date.today()
    warning_items = Todo.query.filter(
        Todo.expiry_date >= today,
        Todo.expiry_date <= today + timedelta(days=5)
    ).order_by(Todo.expiry_date.asc()).all()

    for item in warning_items:
        item.remaining_days = (item.expiry_date - today).days

    return render_template("todo/warning.html",warning_items=warning_items)

@bp.route("/add",methods=["GET","POST"])
@login_required
def add():
    form = TodoForm()

    if form.validate_on_submit():
        todo = Todo(
            expiry_date=form.expiry_date.data,
            title=form.title.data
        )
        db.session.add(todo)
        db.session.commit()
        flash("新しいデータを追加しました。")
        return redirect(url_for("todo.index"))
    return render_template("todo/form.html",form=form,title="商品名を入力")

@bp.route("/<int:id>/edit",methods=["GET","POST"])
@login_required
def edit(id):
    todo = Todo.query.get_or_404(id)
    form = TodoForm(obj=todo)

    if form.validate_on_submit():
        todo.expiry_date = form.expiry_date.data
        todo.title = form.title.data
        db.session.commit()
        flash("データを更新しました。")
        return redirect(url_for("todo.index"))
    return render_template("todo/form.html",form=form,title="データを編集する")

@bp.route("/<int:id>/delete",methods=["POST"])
@login_required
def delete(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    flash("データを削除しました。")
    return redirect(url_for("todo.index"))
