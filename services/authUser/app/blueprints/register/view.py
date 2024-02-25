from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from ...model import User, db
from .form import RegisterForm
from flask_login import current_user
import uuid

register_bp = Blueprint('register_bp', __name__)


@register_bp.route('/register', methods=['POST', 'GET'])
def register_page():
    form = RegisterForm()
    if current_user.is_authenticated:
        flash('You are already logged in!', 'info')
        return redirect(url_for('home_bp.home_page'))
    else:
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user:
                return redirect(url_for('login_bp.login_page'))
            else:
                id = str(uuid.uuid4())
                first_name = form.first_name.data
                last_name = form.last_name.data
                email = form.email.data
                password = generate_password_hash(form.password.data)
                new_user = User(id=id, first_name=first_name, last_name=last_name, email=email, password=password)
                db.session.add(new_user)
                db.session.commit()
                flash('You are registered, Login Now', 'success')
                return redirect(url_for('login_bp.login_page'))
        else:
            print(form.errors)
    return render_template('register.html', form=form)
