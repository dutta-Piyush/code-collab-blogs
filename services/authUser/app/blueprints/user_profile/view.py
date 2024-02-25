from flask import Blueprint, render_template
from flask_login import login_required

userProfile_bp = Blueprint('userProfile_bp', __name__)


@userProfile_bp.route('/profile', methods=['POST', 'GET'])
@login_required
def user_page():
    return render_template('user_profile.html')
