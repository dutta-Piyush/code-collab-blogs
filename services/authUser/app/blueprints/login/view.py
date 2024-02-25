from flask import Blueprint, render_template, redirect, url_for, flash
from .form import LoginForm
from ...model import User
from werkzeug.security import check_password_hash
from flask_login import LoginManager, logout_user, current_user, login_user, login_required

login_bp = Blueprint('login_bp', __name__)
logout_bp = Blueprint('logout_bp', __name__)
login_manager = LoginManager()


@login_manager.user_loader
def user_loader(uid):
    return User.query.get(uid)


@login_manager.unauthorized_handler
def unauthorized():
    flash('You are not logged in. Please log in first.', 'info')
    return redirect(url_for('login_bp.login_page'))


@login_bp.route('/login', methods=['POST', 'GET'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.email == form.email.data and check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
            flash('Hurrey!, You are logged in!', 'success')
            return redirect(url_for('home_bp.home_page'))
        else:
            flash('Email or Password is incorrect!', 'error')
            return redirect(url_for('login_bp.login_page'))
    return render_template('login.html', form=form)


@logout_bp.route('/logout', methods=['POST', 'GET'])
@login_required
def logout_page():
    logout_user()
    flash('You are logged out!', 'success')
    return redirect(url_for('home_bp.home_page'))
