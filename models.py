from routes import app, config
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

class Video(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    mp4path = db.Column(db.String(500), index = True)
    webmpath = db.Column(db.String(500), index = True)

    def __repr__(self):
        return '<Video {0}>'.format(self.webmpath)
