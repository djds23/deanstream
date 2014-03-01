from app import db

class Video(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    mp4path = db.Column(db.String(500), index = True)
    webmpath = db.Column(db.String(500), index = True)

    def get_id(self):
        return str(self.id)

    def get_mp4(self):
        return str(self.mp4path)

    def get_webm(self):
        return str(self.webmpath)

    def __repr__(self):
        return '{0}'.format(get_id)
