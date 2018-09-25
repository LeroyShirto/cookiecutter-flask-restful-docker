# {{cookiecutter.project_name}}

## Build

Docker build

`docker build -t {{cookiecutter.project_name}} Dockerfile`

## Run

Run in production

`docker run --rm -p 8000:8000 {{cookiecutter.project_name}}`

## Running a Shell

To run an interactive Python shell you can use the shell command:

`flask shell`

This will start up an interactive Python shell, setup the correct application context and setup the local variables in the shell. This is done by invoking the [Flask.make_shell_context()](http://flask.pocoo.org/docs/0.12/api/#flask.Flask.make_shell_context) method of the application. By default you have access to your app and [g](http://flask.pocoo.org/docs/0.12/api/#flask.g).

## Components

This flask application makes use of the following great projects

- [Flask_JWT_Extended](https://flask-jwt-extended.readthedocs.io/en/latest/) - A Flask JWT extension that supports refresh tokens, blacklisting/revoking tokens, and token freshness (for accessing critical views)
- [flask-marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/) - An object serialization/deserialization library
- [flask_mongoengine](https://flask-mongoengine.readthedocs.io/en/latest/) - A Flask extension that provides integration with [MongoEngine](http://mongoengine.org/) a mongodb ODM (Object Document Mapper)
- [flask-cors](https://flask-cors.readthedocs.io/en/latest/) - A Flask extension for handling Cross Origin Resource Sharing (CORS)
- [passlib](https://passlib.readthedocs.io/en/stable/) - Passlib is a password hashing library for Python 2 & 3
- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/) - Simple framework for creating REST APIs
- [gunicorn](https://gunicorn.org/) - A Python WSGI HTTP Server for UNIX
