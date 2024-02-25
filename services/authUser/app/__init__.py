from flask import Flask
from .view import home_bp
from .blueprints.login.view import login_bp, logout_bp
from .blueprints.register.view import register_bp
from .blueprints.user_profile.view import userProfile_bp
from .model import db
from .blueprints.login.view import login_manager
from .blueprints.edit_profile.view import editUser_bp


def create_service():
    auth_service = Flask(__name__)

    auth_service.register_blueprint(home_bp, use_prefix='/', templates_folder='templates')
    auth_service.register_blueprint(register_bp, use_prefix='/register', templates_folder='templates')
    auth_service.register_blueprint(login_bp, use_prefix='/login', templates_folder='templates')
    auth_service.register_blueprint(logout_bp, use_prefix='/logout', templates_folder='templates')
    auth_service.register_blueprint(userProfile_bp, use_prefix='/profile', templates_folder='templates')
    auth_service.register_blueprint(editUser_bp, use_prefix='/editProfile', templates_folder='templates')

    # Load configurations from the external file
    auth_service.config.from_object("app.config.Config")

    # Initialize the database
    db.init_app(auth_service)

    # Initialize the LoginManager
    login_manager.init_app(auth_service)

    return auth_service
