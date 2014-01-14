import urllib
from webapp2_extras.appengine.users import login_required

from views.BaseHandler import BaseHandler
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

class UploadMyImage(BaseHandler, blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        upload_files = self.get_uploads('file')  # 'file' is file upload field in the form
        blob_info = upload_files[0]
        self.render_template('my_image_view.html', {'source': str(blob_info.key())})    
    
    @login_required
    def get(self):
        upload_url = blobstore.create_upload_url('/my/image/upload')
        self.render_template('my_image_upload.html', {'upload_url': upload_url})

class GetMyImage(BaseHandler, blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, resource):
        resource = str(urllib.unquote(resource))
        blob_info = blobstore.BlobInfo.get(resource)
        self.send_blob(blob_info)