This is DeanStream! come here to watch different 'streams' of Dean sleeping!
============================================================================

This project is primarially built on Python, Flask, SQLAlchemy, jQuery and a bit of Twitter Bootstrap

This app uses [Pipenv](https://github.com/kennethreitz/pipenv) for dependency management!

To install dependencies, run:

```bash
$ pipenv install
```

To run the site, run:
```bash
$ pipenv run gunicorn run:app
```

visit the site at http://127.0.0.1:8000

To run in debug, add this line to the bottom of 'run.py'

```python
app.run(debug=True)
```

