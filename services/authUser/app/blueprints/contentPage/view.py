from flask import Blueprint, render_template, flash, redirect, url_for
from .form import ContentForm
from ...model import Content, db
from flask_login import login_required, current_user

content_bp = Blueprint('content_bp', __name__)


@content_bp.route('/content', methods=['POST', 'GET'])
@login_required
def content_page():
    form = ContentForm()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            content = Content(title=form.title.data, content=form.body.data, id=current_user.id)
            db.session.add(content)
            db.session.commit()
            flash('The blog is posted successfully', 'success')
            return redirect(url_for('home_bp.home_page'))
        else:
            flash('Please login first!', 'info')
            return redirect(url_for('home_bp.home_page'))
    return render_template('content.html', form=form)
