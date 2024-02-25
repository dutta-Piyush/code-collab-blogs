from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import current_user
from wtforms.validators import DataRequired, Length, Email
from ...model import db
from .form import EditForm
from ...model import User

editUser_bp = Blueprint('editUser_bp', __name__)


@editUser_bp.route('/editProfile/<field_name>', methods=['POST', 'GET'])
def edit_page(field_name):
    form = EditForm()
    # Get the field object from the form
    field = getattr(form, field_name)

    # Clear existing validators
    field.validators = []

    # Apply specific validators based on the field being updated, because in our logic we are updating only one and
    # keeping other static
    if field_name == 'first_name':
        field.validators = [DataRequired(), Length(min=3, max=20)]
    elif field_name == 'last_name':
        field.validators = [DataRequired(), Length(min=3, max=20)]
    elif field_name == 'email':
        field.validators = [DataRequired(), Length(max=30), Email()]

    if form.validate_on_submit():
        if field_name == 'email':
            user = User.query.filter_by(email=form[field_name].data).first()
            if user:
                flash('User already exists', 'error')
                return redirect(url_for('editUser_bp.edit_page', field_name=field_name))
            else:
                setattr(current_user, field_name, form[field_name].data)
                db.session.commit()
                flash(f'{field_name.capitalize()} updated successfully!', 'success')
                return redirect(url_for('userProfile_bp.user_page'))
        else:
            setattr(current_user, field_name, form[field_name].data)
            db.session.commit()
            flash(f'{field_name.capitalize()} updated successfully!', 'success')
            return redirect(url_for('userProfile_bp.user_page'))
    elif request.method == 'GET':
        print("In GET Section")
        print("Field Name", field_name)
        setattr(form, field_name, getattr(current_user, field_name))
    else:
        # Print form errors when validation fails
        print("Validation failed. Form errors:", form.errors)
    return render_template('edit_profile.html', form=form, field_name=field_name)
