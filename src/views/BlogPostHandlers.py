import re

import webapp2
from webapp2_extras.appengine.users import login_required

from models.Blog import Blog, blogGroup
from models.BlogPost import BlogPost
from views.BaseHandler import BaseHandler


PAGE_SIZE = 10
class ListBlogPosts(BaseHandler):
    
    def get(self, blogId):
        bookmark = self.request.get('bookmark')
        blog = Blog.get_by_id(long(blogId), parent=blogGroup())
        blogPosts, newCursor, hasMore = BlogPost.all_for_blog(blog, bookmark)
        for blogPost in blogPosts:
            blogPost.body = CheckForInlineImage.checkImage(blogPost.body)
        taglist = BlogPost.all_tags(blog)
        self.render_template('blog_post_list.html', {'blog': blog, 'blogPosts': blogPosts, 'bookmark': newCursor, 'hasMore': hasMore, 'taglist': taglist})

class GetAllPostsForGivenTag(BaseHandler):
    
    def get(self, blogId, tags):
        bookmark = self.request.get('bookmark')
        blog = Blog.get_by_id(long(blogId), parent=blogGroup())
        blogPosts, newCursor, hasMore = BlogPost.all_for_blog_and_tag(blog, tags, bookmark)
        for blogPost in blogPosts:
            blogPost.body = CheckForInlineImage.checkImage(blogPost.body)
        self.render_template('blog_post_list.html', {'blog': blog, 'blogPosts' : blogPosts, 'bookmark': newCursor, 'hasMore': hasMore})

class ReadBlogPost(BaseHandler):

    def get(self, blogId, postId):
        blog = Blog.get_by_id(long(blogId), parent=blogGroup())
        blogPost = BlogPost.get_by_id(long(postId), parent=blog)
        blogPost.body = CheckForInlineImage.checkImage(blogPost.body)
        self.render_template('blog_post_read.html', {'blog': blog, 'blogPost' : blogPost})
        
class CreateMyBlogPost(BaseHandler):
    
    def post(self, blogId):
        blog = Blog.get_by_id(long(blogId), parent=blogGroup())
        blogPost = BlogPost(blog=blog,
                            title=self.request.get('title'),
                            body=self.request.get('body').encode('ascii', 'ignore'),
                            tags=[x.strip() for x in self.request.get('tags').split(',')],
                            parent=blog)
        blogPost.put()
        return webapp2.redirect("/my/blogs/" + blogId + "/posts")
    
    @login_required
    def get(self, blogId):
        blog = Blog.get_by_id(long(blogId), parent=blogGroup())
        self.render_template('my_blog_post_change.html', {'blog': blog})
        
class EditMyBlogPost(BaseHandler):
    
    def post(self, blogId, postId):
        blog = Blog.get_by_id(long(blogId), parent=blogGroup())
        blogPost = BlogPost.get_by_id(long(postId), parent=blog)
        blogPost.title = self.request.get('title')
        blogPost.body = self.request.get('body').encode('ascii', 'ignore')
        blogPost.tags = [x.strip() for x in self.request.get('tags').split(',')]
        blogPost.put()
        return webapp2.redirect("/my/blogs/" + blogId + "/posts/" + postId)
    
    @login_required
    def get(self, blogId, postId):
        blog = Blog.get_by_id(long(blogId), parent=blogGroup())
        blogPost = BlogPost.get_by_id(long(postId), parent=blog)
        self.render_template('my_blog_post_change.html', {'blog': blog, 'blogPost': blogPost})

class DeleteMyBlogPost(BaseHandler):
    def post(self, blogId, postId):
        blog = Blog.get_by_id(long(blogId), parent=blogGroup())
        blogPost = BlogPost.get_by_id(long(postId), parent=blog)
        blogPost.delete()
        return webapp2.redirect('/my/blogs/' + blogId + '/posts')
    
    @login_required
    def get(self, blogId, postId):
        blog = Blog.get_by_id(long(blogId), parent=blogGroup())
        blogPost = BlogPost.get_by_id(long(postId), parent=blog)
        self.render_template('my_blog_post_delete.html', {'blog': blog, 'blogPost': blogPost})

class ListMyBlogPosts(BaseHandler):
    
    @login_required
    def get(self, blogId):
        bookmark = self.request.get('bookmark')
        blog = Blog.get_by_id(long(blogId), parent=blogGroup())
        blogPosts, newCursor, hasMore = BlogPost.all_for_blog(blog, bookmark)
        taglist = BlogPost.all_tags(blog)
        for blogPost in blogPosts:
            blogPost.body = CheckForInlineImage.checkImage(blogPost.body)
        self.render_template('my_blog_post_list.html', {'blog': blog, 'blogPosts': blogPosts, 'bookmark': newCursor, 'hasMore': hasMore, 'taglist': taglist})

class ReadMyBlogPost(BaseHandler):
     
    @login_required
    def get(self, blogId, postId):
        blog = Blog.get_by_id(long(blogId), parent=blogGroup())
        blogPost = BlogPost.get_by_id(long(postId), parent=blog)
        blogPost.body = CheckForInlineImage.checkImage(blogPost.body)
        self.render_template('my_blog_post_read.html', {'blog': blog, 'blogPost' : blogPost})

class GetMyAllPostsForGivenTag(BaseHandler):
    
    @login_required
    def get(self, blogId, tags):
        bookmark = self.request.get('bookmark')
        blog = Blog.get_by_id(long(blogId), parent=blogGroup())
        blogPosts, newCursor, hasMore = BlogPost.all_for_blog_and_tag(blog, tags, bookmark)
        for blogPost in blogPosts:
            blogPost.body = CheckForInlineImage.checkImage(blogPost.body)
        self.render_template('my_blog_post_list.html', {'blog': blog, 'blogPosts' : blogPosts, 'bookmark': newCursor, 'hasMore': hasMore })

class CheckForInlineImage(BaseHandler):
    @staticmethod
    def checkImage(body):
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', body)
        urlsSet = set(urls)
        if urlsSet:
            for url in urlsSet:
                if url.endswith('.jpg') or url.endswith('.JPG') or url.endswith('.png') or url.endswith('.PNG') or url.endswith('.gif') or url.endswith('.GIF'):
                    newurl = '<img display : inline src = "' + url + '"class="img-responsive" alt="Responsive image"></img>'
                    body = body.replace(url, newurl)
        return body

class GetRSSOfAllPosts(BaseHandler): 
    
    def get(self, blogId): 
        blog = Blog.get_by_id(long(blogId), parent=blogGroup()) 
        blogPosts = BlogPost.everything_for_blog(blog) 
        self.render_template('show_rss.html', {'blog': blog, 'blogPosts' : blogPosts}, 'application/rss+xml')