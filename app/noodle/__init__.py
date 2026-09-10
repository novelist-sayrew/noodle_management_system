from flask import Blueprint

bp = Blueprint("noodle",__name__,template_folder="templates")

from app.noodle import routes