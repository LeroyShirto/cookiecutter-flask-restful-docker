from flask import request, jsonify, Blueprint
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_refresh_token_required,
    get_jwt_identity
)

from {{cookiecutter.app_name}}.models import Users
from {{cookiecutter.app_name}}.schemas import UserSchema
from {{cookiecutter.app_name}}.extensions import pwd_context, jwt

from mongoengine.errors import NotUniqueError

blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@blueprint.route('/login', methods=['POST'])
def login():
    '''Authenticate user and return token
    '''
    if not request.is_json:
        return jsonify({'msg': 'Missing JSON in request'}), 400

    username = request.json.get('username')
    password = request.json.get('password')
    if not username or not password:
        return jsonify({'msg': 'Missing username or password'}), 400

    user = Users.objects.get_or_404(username=username)
    if not pwd_context.verify(password, user.passwd_digest):
        return jsonify({'msg': 'User creds invalid'}), 400

    access_token = create_access_token(identity=str(user.id))
    refresh_token = create_refresh_token(identity=str(user.id))

    ret = {
        'access_token': access_token,
        'refresh_token': refresh_token
    }
    return jsonify(ret), 200


@blueprint.route('/signup', methods=['POST'])
def signup():
    '''Authenticate user and return token
    '''
    if not request.is_json:
        return jsonify({'msg': 'Missing JSON in request'}), 400
    schema = UserSchema()

    user, errors = schema.load(request.json)
    if errors:
        return jsonify(errors), 422
    try:
        user.passwd_digest = pwd_context.hash(user.passwd_digest)
        user.save()
    except NotUniqueError as e:
        return jsonify({'msg': 'User exists with under that email/username'}), 422

    return schema.jsonify(user)


@blueprint.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    ret = {
        'access_token': create_access_token(identity=current_user)
    }
    return jsonify(ret), 200


@jwt.user_loader_callback_loader
def user_loader_callback(identity):
    return User.objects.get(id=identity)
