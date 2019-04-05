import datetime

from {{cookiecutter.project_slug}} import db, marshmallow
from marshmallow import fields, Schema


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(160))
    is_done = db.Column(db.Boolean, default=False)
    posted_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)


class TodoSchema(Schema):
    id = fields.Int(dump_only=True)
    content = fields.Str(required=True)
    is_done = fields.Bool(missing=False)
    posted_on = fields.DateTime(dump_only=True)

    class Meta:
        strict = True
