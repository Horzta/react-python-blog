from flask import Blueprint, redirect, url_for, session
from models import Post
from schemas import PostSchema

api_post = Blueprint('api_post', __name__)


@api_post.route('/api/posts', methods=['GET'])
def index():
    if not session.get('username'):
        return redirect(url_for('user.login'))

    result = Post.query.order_by(Post.id.desc()).all()
    post_schema = PostSchema()

    return post_schema.jsonify(result, many=True)


@api_post.route('/api/post/<id>', methods=['GET'])
def show(id):
    if not session.get('username'):
        return redirect(url_for('user.login'))

    result = Post.query.filter_by(id=id).first()
    post_schema = PostSchema()

    return post_schema.jsonify(result)

