# Notes
[![Build Status](https://app.travis-ci.com/binblee/discover-flask.svg?branch=main)](https://app.travis-ci.com/binblee/discover-flask)

Demo based on [Discover Flask Course](https://github.com/realpython/discover-flask), with Python 3.

### Environment setup

```bash
export DATABASE_URL='postgresql://localhost/discover_flask_dev'
export APP_SETTINGS='config.DevelopmentConfig'
```

`autoenv` is here to automate it.

### Database

Demo is using Postgresql. 

```bash
psql discover_flask_dev
```

### Database migration

Init migration
```bash
flask db init
```

Migrate database
```bash
flask db migrate -m 'version'
flask db upgrade
```

### Unit test

`unittest` style:
```bash
python -m unittest discover -v
```

`pytest` style:
```bash
pytest -v
```


### Test coverage

```bash
coverage run --source=. -m unittest discover
coverage html
```

With pytest-cov introduced, coverage test can also be as follows:
```bash
pytest --cov .
```