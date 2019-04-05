from flask import (
    render_template,
    Blueprint,
)


blueprint = Blueprint('core', __name__)


@blueprint.route('/')
def index():
    return render_template('base.html')
