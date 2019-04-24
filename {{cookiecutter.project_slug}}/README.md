## {{cookiecutter.project_slug}}

[![Build Status](https://travis-ci.org/FILL_UP_your_id/{{cookiecutter.project_slug}}.svg?branch=master)](https://travis-ci.org/FILL_UP_your_id/{{cookiecutter.project_slug}})
[![codecov](https://codecov.io/gh/FILL_UP_your_id/{{cookiecutter.project_slug}}/branch/master/graph/badge.svg)](https://codecov.io/gh/FILL_UP_your_id/{{cookiecutter.project_slug}})


### Running the app locally


```
# Create and activate virutal environment.
# It need not be necessarily in the project directory.
python -m venv .venv
source .venv/bin/activate

# Install dependencies.
pip install -r requirements/local.txt

# Create .env file and modify it for your setup.
# Most settings have default values.
# Look in {{cookiecutter.project_slug}}/settings.py for details.
cp .env.example .env

# You will need to create the development and test database manually.
# Once the database is configured, migrations need to run.
flask db init
flask db migrate
flask db upgrade

# webpack is used to manage assets.
# Static files under static folder works without webpack.
# But webpack does nice things like bundle creation, fingerpriting etc.
# Run webpack in watch mode to continously recompile assets.
npm run watch

# Run the flask application.
# FLASK_APP and FLASK_DEBUG is already set in .flaskenv
flask run
```

### Deployment

Generate webpack assets in production mode.

```
# Create webpack assets.
npm build
```

The rest of the deployment is for a regular flask application. Change `.env` for your settings and then run the `Procfile` through a PaaS, or through `honcho`, or through any other wsgi server.


### Assets management

webpack is used for asset management. The generated manifest is read and the names are used in the templates. Check `webpack.config.js` and `base.html` for details.

