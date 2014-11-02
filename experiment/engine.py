from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts

class PostEngine:

	def __init__(self, url, user, password, image_folder_path):
		self.url = url
		self.user = user
		self.password = password
		self.image_folder_path = image_folder_path
		self.client = Client( url, user, password)

	def upload(self, file_name):
		file_path = self.image_folder_path + '/' + file_name
		data = { 'name' : file_name, 'type' : 'image/jpeg' }

        with open(file_path, 'rb') as img:
            data['bits'] = xmlrpc_client.Binary(img.read())


        response = self.client.call(media.UploadFile(data))
		return response;

	def post():
		return None;

	def uploadFeatureImage(file_path):
		return None;

	def uploadProductImage(file_path):
		return None;
