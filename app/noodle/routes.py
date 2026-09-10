from flask import render_template,redirect,url_for,flash,request
from flask_login import login_required,current_user
from app.noodle import bp
from app import db
from app.models import Noodle
from app.forms import NoodleForm
from datetime import date,datetime,timedelta

@bp.route("/")
@login_required
def index():
    noodles = Noodle.query.order_by(Noodle.expiry_date.asc()).all()
    today = date.today()

    for noodle in noodles:
        noodle.remaining_days = (noodle.expiry_date - today).days
    expired_items = Noodle.query.filter(Noodle.expiry_date < today).all()
    return render_template("noodle/list.html",noodles=noodles,expired_items=expired_items)

@bp.route("/warning")
@login_required
def warning():
    today = date.today()
    warning_items = Noodle.query.filter(
        Noodle.expiry_date >= today,
        Noodle.expiry_date <= today + timedelta(days=5)
    ).order_by(Noodle.expiry_date.asc()).all()

    for item in warning_items:
        item.remaining_days = (item.expiry_date - today).days

    return render_template("noodle/warning.html",warning_items=warning_items)

@bp.route("/add",methods=["GET","POST"])
@login_required
def add():
    form = NoodleForm()

    if form.validate_on_submit():
        noodle = Noodle(
            expiry_date=form.expiry_date.data,
            name=form.name.data
        )
        db.session.add(noodle)
        db.session.commit()
        flash("新しいデータを追加しました。")
        return redirect(url_for("noodle.index"))
    return render_template("noodle/form.html",form=form,title="商品名を入力")

@bp.route("/<int:id>/edit",methods=["GET","POST"])
@login_required
def edit(id):
    noodle = Noodle.query.get_or_404(id)
    form = NoodleForm(obj=noodle)

    if form.validate_on_submit():
        noodle.expiry_date = form.expiry_date.data
        noodle.name = form.name.data
        db.session.commit()
        flash("データを更新しました。")
        return redirect(url_for("noodle.index"))
    return render_template("noodle/form.html",form=form,title="データを編集する")

@bp.route("/<int:id>/delete",methods=["POST"])
@login_required
def delete(id):
    noodle = Noodle.query.get_or_404(id)
    db.session.delete(noodle)
    db.session.commit()
    flash("データを削除しました。")
    return redirect(url_for("noodle.index"))
