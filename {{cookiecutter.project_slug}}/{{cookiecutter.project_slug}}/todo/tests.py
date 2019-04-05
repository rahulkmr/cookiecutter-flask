import random

from flask import url_for

import pytest

from {{cookiecutter.project_slug}} import db
from {{cookiecutter.project_slug}}.todo.models import Todo


todos = (
    Todo(content='write some tests', is_done=False),
    Todo(content='integrate swagger ui', is_done=False),
    Todo(content='convert to cookiecutter', is_done=False),
    Todo(content='implement a basic api', is_done=True),
    Todo(content='integrate webpack assets', is_done=True),
)


def setup_module(module):
    for todo in todos:
        db.session.add(todo)
    db.session.commit()


def teardown_module(module):
    for todo in todos:
        db.session.delete(todo)
    db.session.commit()


def test_index_and_show(client):
    result = client.get(url_for('todo_api.todo_index')).get_json()

    assert len(result) == len(todos)

    for counter in range(len(result) // 2):
        choice = random.choice(result)
        fetched = client.get(
            url_for('todo_api.todo_show', id=choice['id'])).get_json()
        assert choice['id'] == fetched['id'] and \
            choice['content'] == fetched['content'] and \
            choice['is_done'] == fetched['is_done']


def test_create_update_and_delete(client):
    content = 'new todo'
    result = client.post(url_for('todo_api.todo_create'),
                         json={'content': content}).get_json()
    assert result['content'] == content and result['is_done'] == False

    updated = client.put(url_for('todo_api.todo_update', id=result['id']),
                         json={'content': 'updated content'}).get_json()
    assert updated['content'] == 'updated content'

    client.delete(url_for('todo_api.todo_delete', id=result['id']))
    assert client.get(url_for('todo_api.todo_show',
                              id=result['id'])).get_json() == {}
