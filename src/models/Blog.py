from google.appengine.ext import db


def blogGroup():
    return db.Key.from_path('BlogGroupName', 'default_name')

class Blog(db.Model):
    author = db.UserProperty()
    title = db.StringProperty()
    created_on = db.DateTimeProperty(auto_now_add=True)
    
    @staticmethod
    def all_for_author(author):
        q = db.Query(Blog)
        q.ancestor(blogGroup())
        q.filter('author = ', author)
        q.order('-created_on')
        return q
