from flask import Blueprint, render_template
from .model import Content

home_bp = Blueprint('home_bp', __name__)


@home_bp.route('/')
@home_bp.route('/home')
def home_page():
    contents = Content.query.all()
    return render_template('home.html', contents=contents)
