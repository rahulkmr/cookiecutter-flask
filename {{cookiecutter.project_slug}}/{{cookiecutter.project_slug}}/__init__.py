from flask import (
    Flask,
    Blueprint,
    g,
)

from flask_talisman import Talisman
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache
from flask_security import (
    Security,
    SQLAlchemyUserDatastore,
)
from flask_mail import Mail
from flask_babel import Babel
from flask_marshmallow import Marshmallow
from flask_apispec import FlaskApiSpec

from werkzeug.middleware.proxy_fix import ProxyFix

from whitenoise import WhiteNoise
{%- if cookiecutter.use_celery == 'y' %}
from celery import Celery
{%- endif %}

from . import settings
from .middlewares import (
    HTTPMethodOverrideMiddleware,
)
from .extensions import (
    Webpack,
)
from . import commands


db = SQLAlchemy()
cache = Cache()
user_datastore = None
security = None
mail = Mail()
babel = Babel()
marshmallow = Marshmallow()
api_spec = FlaskApiSpec()
{%- if cookiecutter.use_celery == 'y' %}
celery = Celery(__name__, broker=settings.CELERY_BROKER_URL,
                backend=settings.CELERY_RESULT_BACKEND)
{%- endif %}


def create_app(config_object=settings):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_middlewares(app)
    register_commands(app)
    init_security(app)
    register_blueprints(app)
    {%- if cookiecutter.use_celery == 'y' %}
    register_tasks(app)
    {%- endif %}

    return app


def register_extensions(app):
    # Talisman(app)

    db.init_app(app)
    Migrate(app, db)

    if app.debug:
        from flask_debugtoolbar import DebugToolbarExtension
        DebugToolbarExtension(app)

    cache.init_app(app)
    mail.init_app(app)
    babel.init_app(app)
    marshmallow.init_app(app)
    api_spec.init_app(app)

    {%- if cookiecutter.use_celery == 'y' %}
    make_celery(app)
    {%- endif %}

    Webpack(app)


def register_middlewares(app):
    app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)
    app.wsgi_app = ProxyFix(app.wsgi_app)

    app.wsgi_app = WhiteNoise(app.wsgi_app)
    static_folders = (
        '{{cookiecutter.project_slug}}/static/',
        # Add blueprint static folders here.
    )
    for static in static_folders:
        app.wsgi_app.add_files(static)


def init_security(app):
    from . import models
    global user_datastore, security
    user_datastore = SQLAlchemyUserDatastore(db,
                                             models.User,
                                             models.Role)
    security = Security(app, user_datastore)


def register_blueprints(app):
    import {{cookiecutter.project_slug}}.core.views as core_views
    app.register_blueprint(core_views.blueprint, url_prefix='/')

    import {{cookiecutter.project_slug}}.todo.views as todo_views
    app.register_blueprint(todo_views.blueprint, url_prefix='/api/v1/')
    todo_views.register_endpoints_with_swagger()


def register_commands(app):
    commands.register(app)


{% if cookiecutter.use_celery == 'y' %}
def make_celery(app):
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


def register_tasks(app):
    from . import tasks
{% endif %}
