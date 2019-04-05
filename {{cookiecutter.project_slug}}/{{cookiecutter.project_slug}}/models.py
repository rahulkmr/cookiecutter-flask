from flask_security import UserMixin, RoleMixin

from {{cookiecutter.project_slug}} import (
    db,
)


role_user = db.Table('role_user',
                     db.Column('user_id',
                               db.Integer(),
                               db.ForeignKey('user.id')),
                     db.Column('role_id',
                               db.Integer(),
                               db.ForeignKey('role.id')))



class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(16))
    current_login_ip = db.Column(db.String(16))
    login_count = db.Column(db.Integer)

    roles = db.relationship('Role', secondary=role_user,
                            backref=db.backref('users', lazy='dynamic'))
