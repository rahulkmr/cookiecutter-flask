from {{cookiecutter.project_slug}}.settings import *

TESTING = True
DEBUG = False
SQLALCHEMY_DATABASE_URI = 'postgresql:///{{cookiecutter.project_slug}}_test'
SQLALCHEMY_TRACK_MODIFICATIONS = False
WTF_CSRF_ENABLED = False
