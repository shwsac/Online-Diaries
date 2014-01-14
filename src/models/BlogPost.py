from google.appengine.datastore.datastore_query import Cursor
from google.appengine.ext import db

from models.Blog import Blog


PAGE_SIZE = 10
class BlogPost(db.Model):
    blog = db.ReferenceProperty(Blog, collection_name = 'posts')
    #author = db.UserProperty()
    title = db.StringProperty(required = True)
    body = db.BlobProperty(required = True)
    tags = db.StringListProperty()
    created_on = db.DateTimeProperty(auto_now_add=True)
    modified_on = db.DateTimeProperty(auto_now=True)
    
    @staticmethod
    def all_for_blog(blog, cursorStr=None):
        cursor = None
        if cursorStr:
            cursor = Cursor.from_websafe_string(cursorStr)
        q = db.Query(BlogPost)
        q.ancestor(blog)
        q.filter('blog = ', blog)
        q.order('-created_on')
        result = q.fetch(PAGE_SIZE, start_cursor=cursor)
        newCursorStr = q.cursor()
        hasMore = len(q.fetch(1, start_cursor=Cursor.from_websafe_string(newCursorStr)))
        return result, newCursorStr, hasMore > 0
  
    @staticmethod
    def all_for_blog_and_tag(blog, tags, cursorStr=None):
        cursor = None
        if cursorStr:
            cursor = Cursor.from_websafe_string(cursorStr)
        q = db.Query(BlogPost)
        q.ancestor(blog)
        q.filter('blog = ', blog)
        q.filter('tags = ', tags)
        q.order('-created_on')
        result = q.fetch(PAGE_SIZE, start_cursor=cursor)
        newCursorStr = q.cursor()
        hasMore = len(q.fetch(1, start_cursor=Cursor.from_websafe_string(newCursorStr)))
        return result, newCursorStr, hasMore > 0
    
    @staticmethod
    def all_tags(blog):
        q = db.GqlQuery("SELECT tags FROM BlogPost WHERE blog = :1 AND ANCESTOR IS :2", blog, blog)
        tagslist = []
        for projection in q:
            tagslist.extend(projection.tags)
        return set(tagslist)
      
    @staticmethod
    def everything_for_blog(blog):
        q = BlogPost.all()
        q.ancestor(blog)
        q.filter('blog = ', blog)
        return q
                     
        