from datetime import datetime
from models import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(80), unique=False, nullable=False)
    content = db.Column(db.Text(), unique=False, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.title+":"+self.content)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return
