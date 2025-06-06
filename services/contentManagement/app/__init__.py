from flask import Flask
from .blueprints.contentPage.view import content_bp
from .model import db


def create_service2():
    content_service = Flask(__name__)

    content_service.register_blueprint(content_bp, use_prefix='/', template_folder='templates')

    # Load Config from Class file
    content_service.config.from_object("app.config.ProjConfig")

    db.init_app(content_service)

    return content_service
