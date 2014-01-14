import os
 
from google.appengine.api import users
import jinja2
import webapp2
import urlparse
 
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), '../templates')
jinja_environment = \
    jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))


class BaseHandler(webapp2.RequestHandler):
     
    def render_template(
        self,
        filename,
        template_values,
        content_type = None,
        **template_args
        ):
        user = users.get_current_user()
        template_values['loginUrl'] = users.create_login_url(".")
        template_values['logoutUrl'] = users.create_logout_url(".")
        template_values['user'] = user
        o = urlparse.urlparse(self.request.url)
        baseUrl = urlparse.urlunparse((o.scheme, o.netloc, '', '', '', ''))
        template_values['baseUrl'] = baseUrl
        template_values['request'] = self.request
        template = jinja_environment.get_template(filename)
        if content_type:
            self.response.headers['Content-Type'] = content_type
        self.response.out.write(template.render(template_values))