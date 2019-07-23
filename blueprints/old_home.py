from flask import Blueprint, request, render_template, redirect, url_for, session
from models import Post


old_home = Blueprint('old_home', __name__)


@old_home.route('/old/', methods=['GET', 'POST'])
def index():
    if not session.get('username'):
        return redirect(url_for('user.login'))

    if request.method == "POST":
        post = Post(title=request.form['title'], content=request.form['content'], user_id=session['user_id'])
        post.save()
        return redirect(url_for('old_home.index'))

    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('index.html', username=session['username'], posts=posts)
