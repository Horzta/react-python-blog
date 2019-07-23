from flask import Blueprint, request, render_template, redirect, url_for, session
from models.user import User

user = Blueprint('user', __name__)


@user.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username, password=password).first()
        if user is None:
            return render_template('login.html', error='Invalid Username/Password')
        else:
            session['username'] = username
            session['user_id'] = user.id
            return redirect(url_for('old_home.index'))

    return render_template('login.html')


@user.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('user.login'))


@user.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        new_user = User(username=username, email=email, password=password)
        new_user.save()
        return redirect(url_for('old_home.index'))

    return render_template('register.html')


@user.route('/users/', methods=['GET'])
def users():
    return render_template('users.html', users=User.query.all())
