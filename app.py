from flask import Flask
from blueprints.old_home import old_home
from blueprints.user import user
from blueprints.api_post import api_post
from blueprints.api_user import api_user
from blueprints.react import react

app = Flask(__name__)
app.register_blueprint(react)
app.register_blueprint(old_home)
app.register_blueprint(user)
app.register_blueprint(api_post)
app.register_blueprint(api_user)


app.secret_key = "!!!!!@#$%^&*()!!!"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


from models import db
db.init_app(app)

from schemas import ma
ma.init_app(app)



