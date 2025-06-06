from flask import Blueprint, render_template
from ...model import Content

content_bp = Blueprint('content_bp', __name__)


@content_bp.route('/', methods=['POST', 'GET'])
def content_page():
    contents = Content.query.all()
    for content in contents:
        print(content)
        print(content.id)
        print(content.title)
        print()
    return render_template('temp_index.html', contents=contents)
