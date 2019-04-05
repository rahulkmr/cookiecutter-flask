from flask import Blueprint, jsonify, request, current_app
from flask.views import MethodView

from flask_apispec import use_kwargs, marshal_with

from {{cookiecutter.project_slug}} import db

from .models import Todo, TodoSchema


blueprint_name = 'todo_api'
blueprint = Blueprint(blueprint_name, __name__)


@blueprint.route('/todos/')
@marshal_with(TodoSchema(many=True))
def todo_index():
    return Todo.query.all()


@blueprint.route('/todos/<int:id>/')
@marshal_with(TodoSchema)
def todo_show(id):
    return Todo.query.get(id)


@blueprint.route('/todos/<int:id>/', methods=['DELETE'])
@marshal_with(None, code=204)
def todo_delete(id):
    todo = Todo.query.get(id)
    db.session.delete(todo)
    db.session.commit()
    return None


@blueprint.route('/todos/<int:id>/', methods=['PUT'])
@use_kwargs(TodoSchema)
@marshal_with(TodoSchema)
def todo_update(id, **updated_todo):
    todo = Todo.query.get(id)
    todo.content = updated_todo['content']
    db.session.add(todo)
    db.session.commit()

    return todo


@blueprint.route('/todos/', methods=['POST'])
@use_kwargs(TodoSchema)
@marshal_with(TodoSchema)
def todo_create(**new_todo):
    todo = Todo(**new_todo)
    db.session.add(todo)
    db.session.commit()
    return todo


def register_endpoints_with_swagger():
    from {{cookiecutter.project_slug}} import api_spec
    for target, endpoint in (
        (todo_show, 'todo_show'),
        (todo_index, 'todo_index'),
        (todo_update, 'todo_update'),
        (todo_create, 'todo_create'),
        (todo_delete, 'todo_delete')):
        api_spec.register(target, endpoint, blueprint_name)
