from {{cookiecutter.app_name}}.helpers import Env

DEBUG = Env.bool('DEBUG', False)
SECRET_KEY = Env.string('SECRET_KEY', 'changeme')

MONGODB_HOST = Env.string('MONGODB_HOST', 'mongo')
MONGODB_PORT = Env.int('MONGODB_PORT', 27017)
MONGODB_NAME = Env.string('MONGODB_NAME', '{{cookiecutter.app_name|lower|replace(' ', '_')|replace("-", "_")}}')

MONGODB_SETTINGS = [{
    'db': MONGODB_NAME,
    'host': MONGODB_HOST,
    'port': MONGODB_PORT
}]
