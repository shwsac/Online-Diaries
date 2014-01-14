from google.appengine.ext import db

class BlogPost(db.Model):
    image = db.BlobProperty()
    user = db.UserProperty()