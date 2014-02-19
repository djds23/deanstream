from routes import app, config
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

class Video(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    mp4path = db.Column(db.String(500), index = True)
    webmpath = db.Column(db.String(500), index = True)

    def get_mp4(self):
        return unicode(self.mp4path)

    def get_webm(self):
        return unicode(self.webmpath)

    def __repr__(self):
        return '<Video {0},{1}>'.format(self.mp4path, self.webmpath)
