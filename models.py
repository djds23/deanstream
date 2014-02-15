from routes import db

class Video(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    mp4_path = db.Column(db.String(500), index = True, unique = True)
    webm_path = db.Column(db.String(500), index = True, unique = True)

    def __repr__(self):
        return '<Video r%>' % webm_path
