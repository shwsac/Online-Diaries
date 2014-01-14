Online-Diaries
==============
Overview: Project is developed using Google App Engine’s Python API, datastore, Jinja2 templates, bootstrap frontend framework, webapp2 python web framework. Following are brief introduction to these environments: 
Google App Engine lets you run web applications on Google's infrastructure. App Engine applications are easy to build, easy to maintain, and easy to scale as your traffic and data storage needs grow. With App Engine, there are no servers to maintain: You just upload your application, and it's ready to serve your users.
Google App Engine makes it easy to build an application that runs reliably, even under heavy load and with large amounts of data. App Engine includes the following features:
•	dynamic web serving, with full support for common web technologies
•	persistent storage with queries, sorting and transactions
•	automatic scaling and load balancing
•	APIs for authenticating users and sending email using Google Accounts
•	a fully featured local development environment that simulates Google App Engine on your computer
•	task queues for performing work outside of the scope of a web request
•	scheduled tasks for triggering events at specified times and regular intervals

App Engine executes your Python application code using a pre-loaded Python interpreter in a safe "sandboxed" environment. Your app receives web requests, performs work, and sends responses by interacting with this environment
The DataStore
Apps can use the App Engine Datastore for reliable, scalable persistent storage of data. The Python API to the App Engine datastore includes rich data modeling tools for managing data schemas. The API supports two interfaces for performing datastore queries, including GQL, a SQL-like query language that is also used in the Admin Console.
The App Engine Memcache provides fast, transient distributed storage for caching the results of datastore queries and calculations. The Python interface to the App Engine memcache is compatible with the Python Memcached API.
Apps use the URL Fetch service to access resources over the web, and to communicate with other hosts using the HTTP and HTTPS protocols. Python applications can use theurllib, urllib2, or httplib modules from the Python standard library to access this service, or they can use the App Engine URL Fetch service API.

The Images service lets applications transform and manipulate image data in several formats, including cropping, rotating, resizing, and photo color enhancement.

An application can use Google Accounts for user authentication. Google Accounts handles user account creation and sign-in, and a user that already has a Google account (such as a Gmail account) can use that account with your app. An app can detect when the current user is signed in, and can access the user's email address. The Python API can return user data in an object that can be stored directly in the datastore.

Jinja2 is a modern and designer friendly templating language for Python, modelled after Django’s templates. It is fast, widely used and secure with the optional sandboxed template execution environment

Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.
Bootstrap is a free collection of tools for creating websites and web applications. It contains HTML and CSS-based design templates for typography, forms, buttons, navigation and other interface components, as well as optional JavaScript extensions.
Application Design:
The main page of application lists all blogs hosted on the site. Site handles multiple users and each user can create one or more blogs. On main page we have option to login/logout of user account. Once logged in main page shows option to view ‘My Dashboard’ which redirects to page which lists all blogs owned by user. Also It shows welcome message as ‘hi, username’.
List of blogs on main page also displays author of each blog and the creation date of blog. We can click on any blog and can see the list of blogposts. Blogs can be viewed without an account or login. At most 10 posts are shown on a page, with a link to go to the next page of older posts.
When multiple posts are there on the same page of the standard blog view, each post displays the content capped at 500 characters.  Each post also have a "permalink" that, when followed, shows the complete content of the post on its own page.
All tags given for various posts in a blog are listed at the bottom of the blog page. We can click on any tag to see all posts which are given the same tag.
Once the user logs in, he can go to ‘My Dashboard’ to view all blogs owned by that user. Dashboard will also have an option to create new blog or edit or delete existing blog. When user clicks on create new blog it takes user to another page where user can enter name for blog. Blog can have multiple posts. Each blog has option to create new post. Each post can be viewed as permalink on new page. User also have an option to edit or delete post. Post has two timestamps associated with it as creation time and modification time. 

Blog contains blogposts which can be inline images or uploaded image’s permalinks.
User can attach tags for any post. 
Apart from post user can upload any image they want. Image gets unique permalink which can be used and can be added in any post. User can write any http or https links inside post. If link is image, image is shown as inline image. 
Each blog also has RSS link which dumps blog in xml format.
Application Modules:
Design is in the form of model template view architecture. Model contains the storage model in db.model format. It has following model classes:
Blog: It holds data related to blog as Author of blog, name of blog and time the blog is created.
BlogPost: It stores data related to blog posts as title of post, body of post, tags attached to the post and creation and modification timestamp of post. Further it also links the post data to blog by reference property.
In view we have BaseHandler. It holds the render_template function which has the basic layout for pages which will be displayed on browser. It displays login/logout url as well as name of user which logged in. Further it displays integration with social media like twitter facebook google+ etc
BlogHandler: This module holds various classes to display and modify blogs.

-	ListBlogs – Get all blogs from Blog.py and renders blog_list.html which displays the list along with author and created time as a table.
-	ListMyBlogs – Gets blogs of specified user and renders my_blog_list.html which lists blogs of user and option to create new blog.
-	CreateMyBlog and EditMyBlog - Renders my_blog_change.html which allows to create new blog or edit existing blog.
-	DeleteMyBlog – Renders my_blog_delete.html to delete given blog.  
-	BlogPostHandlers: This module holds various classes to display and edit posts and images.
-	ListBlogPosts – Gets all posts for given blog and rendeers blog_post_list.html to display them.
-	GetAllPostsForGivenTag -  Gets all posts for given tag and renders blog_post_list.html to display them.
-	ReadBlogPost – For given post of blog renders blog_post_read.html to view full post.
-	CreateMyBlogPost and EditMyBlogPost - For given blog of user renders my_blog_post_change.html to create new blog post or edit existing.
-	DeleteMyBlogPost – Renders my_blog_post_delete.html to confirm if user wants to delete the post.
-	ListMyBlogPosts – Gets all posts for given blog of user and renders my_blog_post_list.html to display them. It also allows to create new post or upload new image.
-	ReadMyBlogPost - For given post of blog renders my_blog_post_read.html to view full post. It also provides option to edit or delete the post.
-	GetMyAllPostsForGivenTag - Gets all posts for given tag for user and renders my_blog_post_list.html to display them.
-	CheckForInlineImage –  Checks if the URL entered in post body is of image.
-	GetRSSOfAllPosts – Calls show_rss.html to dump blog into xml format.

ImageHandler: This module holds following two classes to upload and store image.
-	UploadMyImage – Calls my_image_upload.html to get the file of image from user.
-	GetMyImage – Calls my_image_view.html to get URL of image and view it. 



