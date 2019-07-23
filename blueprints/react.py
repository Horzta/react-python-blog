from flask import Blueprint, render_template, redirect, url_for, session


react = Blueprint('react', __name__)


@react.route('/', methods=['GET'])
def index():
    if not session.get('username'):
        return redirect(url_for('user.login'))

    return render_template('react/App.html', username=session['username'])
