"""
Application configuration.

Most configuration are set via environment variables.
Use a .env file in the project root to change configuration.
"""
from environs import Env

env = Env()
env.read_env()

TESTING = env.bool('TESTING', False)
SECRET_KEY = env.str('SECRET_KEY')
CACHE_TYPE = env.str('CACHE_TYPE', 'simple')

# flask-sqlalchemy configs
database_url = env.str('SQLALCHEMY_DATABASE_URI', None) or \
    env.str('DATABASE_URL', None) or \
    'postgresql:///{{cookiecutter.project_slug}}'
SQLALCHEMY_DATABASE_URI = database_url
in_development = env.str('FLASK_ENV', '') == 'development'
SQLALCHEMY_TRACK_MODIFICATIONS = in_development

# flask-security configs
SECURITY_URL_PREFIX = env.str('SECURITY_URL_PREFIX', '/account')
SECURITY_CONFIRMABLE = env.bool('SECURITY_CONFIRMABLE', True)
SECURITY_REGISTERABLE = env.bool('SECURITY_REGISTERABLE', True)
SECURITY_RECOVERABLE = env.bool('SECURITY_RECOVERABLE', True)
SECURITY_TRACKABLE = env.bool('SECURITY_TRACKABLE', True)
SECURITY_CHANGEABLE = env.bool('SECURITY_CHANGEABLE', True)
SECURITY_PASSWORD_SALT = env.str('SECURITY_PASSWORD_SALT')


# flask-mail configs
MAIL_SERVER = env.str('MAIL_SERVER', 'localhost')
MAIL_PORT = env.int('MAIL_PORT', 25)
MAIL_USE_TLS = env.bool('MAIL_USE_TLS', True)
MAIL_USERNAME = env.str('MAIL_USERNAME', '')
MAIL_PASSWORD = env.str('MAIL_PASSWORD', '')
MAIL_DEFAULT_SENDER = env.list('MAIL_DEFAULT_SENDER',
                               ['{{ cookiecutter.name }}', '{{ cookiecutter.email }}'])

# webpack configs
WEBPACK_MANIFEST_PATH = env.str('WEBPACK_MANIFEST_PATH',
                                './static/build/manifest.json')
WEBPACK_ASSETS_BASE_URL = env.str('WEBPACK_ASSETS_BASE_URL', None)

APISPEC_TITLE = env.str('APISPEC_TITLE', '{{ cookiecutter.project_slug }}')

{%- if cookiecutter.use_celery == 'y' %}
CELERY_BROKER_URL = env.str('CELERY_BROKER_URL',
                            'redis://localhost:6379')
CELERY_RESULT_BACKEND = env.str('CELERY_RESULT_BACKEND',
                                'redis://localhost:6379')
{%- endif %}
