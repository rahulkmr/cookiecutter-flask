

def test_config_value(app):
    assert app.config['TESTING'] is True
    assert app.config['DEBUG'] is False
    assert app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] is False
