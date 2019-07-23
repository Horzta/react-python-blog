from flask import Blueprint, redirect, url_for, session
from models import User
from schemas import UserSchema

api_user = Blueprint('api_user', __name__)


@api_user.route('/api/users', methods=['GET'])
def index():
    if not session.get('username'):
        return redirect(url_for('user.login'))

    result = User.query.order_by(User.id.desc()).all()
    user_schema = UserSchema()

    return user_schema.jsonify(result, many=True)


@api_user.route('/api/user/<id>', methods=['GET'])
def show(id):
    if not session.get('username'):
        return redirect(url_for('user.login'))

    result = User.query.filter_by(id=id).first()
    user_schema = UserSchema()

    return user_schema.jsonify(result)
