from flask import Blueprint, render_template
from flask_login import login_required, current_user
from ...model import Content

userProfile_bp = Blueprint('userProfile_bp', __name__)


@userProfile_bp.route('/profile', methods=['POST', 'GET'])
@login_required
def user_page():
    user_content = Content.query.filter_by(id=current_user.id)
    return render_template('user_profile.html', user_content=user_content)
