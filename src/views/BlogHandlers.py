
from datetime import datetime

from google.appengine.api import users
import webapp2
from webapp2_extras.appengine.users import login_required

from models.Blog import Blog, blogGroup
from views.BaseHandler import BaseHandler


class ListBlogs(BaseHandler):
    def get(self):
        blogs = Blog.all();
        blogs.ancestor(blogGroup())
        self.render_template('blog_list.html', {'blogs': blogs})

class ListMyBlogs(BaseHandler):
    @login_required
    def get(self):
        user = users.get_current_user()
        blogs = Blog.all_for_author(user)
        self.render_template('my_blog_list.html', {'blogs': blogs})

class CreateMyBlog(BaseHandler):
    def post(self):
        user = users.get_current_user()
        blog = Blog(parent=blogGroup(), author = user, title = self.request.get('title'), name = self.request.get('name'), created_on = datetime.now())
        blog.put()
        return webapp2.redirect('/my/blogs')
    
    @login_required
    def get(self):
        self.render_template('my_blog_change.html', {})

class EditMyBlog(BaseHandler):
    def post(self, blogId):
        blog = Blog.get_by_id(long(blogId), parent=blogGroup())
        blog.title = self.request.get('title')
        blog.put()
        return webapp2.redirect('/my/blogs')
    
    @login_required
    def get(self, blogId):
        blog = Blog.get_by_id(long(blogId), parent=blogGroup())
        self.render_template('my_blog_change.html', {'blog': blog})
        
class DeleteMyBlog(BaseHandler):
    def post(self, blogId):
        blog = Blog.get_by_id(long(blogId), parent=blogGroup())
        for post in blog.posts:
            post.delete()
        blog.delete()
        return webapp2.redirect('/my/blogs')
    
    @login_required
    def get(self, blogId):
        blog = Blog.get_by_id(long(blogId), parent=blogGroup())
        self.render_template('my_blog_delete.html', {'blog': blog})