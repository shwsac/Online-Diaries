from webapp2 import Route, RedirectHandler
import webapp2

from views.BlogHandlers import ListBlogs, ListMyBlogs, CreateMyBlog, EditMyBlog, \
    DeleteMyBlog
from views.BlogPostHandlers import CreateMyBlogPost, EditMyBlogPost, \
    ListBlogPosts, ReadBlogPost, ListMyBlogPosts, ReadMyBlogPost, DeleteMyBlogPost, \
    GetMyAllPostsForGivenTag, GetAllPostsForGivenTag, GetRSSOfAllPosts
from views.ImageHandler import GetMyImage, UploadMyImage

# from google.appengine.ext.webapp.util import run_wsgi_app
application = webapp2.WSGIApplication([Route(r'/', RedirectHandler, defaults={'_uri': '/blogs'}),
                                       Route(r'/blogs', ListBlogs),
                                       Route(r'/blogs/<blogId:\d+>/posts', ListBlogPosts),
                                       Route(r'/blogs/<blogId:\d+>/posts/rss', GetRSSOfAllPosts),
                                       Route(r'/blogs/<blogId:\d+>/posts/<postId:\d+>', ReadBlogPost),
                                       Route(r'/blogs/<blogId:\d+>/posts/tag/<tags:.+>', GetAllPostsForGivenTag),
                                       Route(r'/my/', RedirectHandler, defaults={'_uri': '/my/blogs'}),
                                       Route(r'/my/blogs', ListMyBlogs),
                                       Route(r'/my/blogs/create', CreateMyBlog),
                                       Route(r'/my/blogs/<blogId:\d+>/edit', EditMyBlog),
                                       Route(r'/my/blogs/<blogId:\d+>/delete', DeleteMyBlog),
                                       Route(r'/my/blogs/<blogId:\d+>/posts', ListMyBlogPosts),
                                       Route(r'/my/blogs/<blogId:\d+>/posts/rss', GetRSSOfAllPosts),
                                       Route(r'/my/image/upload', UploadMyImage),
                                       Route(r'/my/image/get/<resource:.+>', GetMyImage),
                                       Route(r'/my/blogs/<blogId:\d+>/posts/create', CreateMyBlogPost),
                                       Route(r'/my/blogs/<blogId:\d+>/posts/<postId:\d+>', ReadMyBlogPost),
                                       Route(r'/my/blogs/<blogId:\d+>/posts/<postId:\d+>/edit', EditMyBlogPost),
                                       Route(r'/my/blogs/<blogId:\d+>/posts/<postId:\d+>/delete', DeleteMyBlogPost),
                                       Route(r'/my/blogs/<blogId:\d+>/posts/tag/<tags:.+>', GetMyAllPostsForGivenTag)], debug=True)