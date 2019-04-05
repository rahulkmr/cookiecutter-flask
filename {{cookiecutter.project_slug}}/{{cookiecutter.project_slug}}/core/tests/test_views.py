

def test_index_page(client):
    result = client.get('/')
    assert b'{{cookiecutter.project_slug}}' in result.data
