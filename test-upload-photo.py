import unittest
from experiment import engine
 


# Here's our "unit tests"
class testPostEngine(unittest.TestCase):

	def setUp(self):

		self.webUrl = 'http://localhost:8888/trakulthai'
		self.image_folder = 'product_images'

		self.doer = engine.PostEngine( self.webUrl + '/xmlrpc.php'
			, 'admin'
			, '123456'
			, self.image_folder);

	def test_Upload(self):
		product_id = 'AS123b'
		file_name = product_id + '.jpg'

		response = self.doer.upload(file_name)

		self.assertEqual(response.file, file_name)
		self.assertEqual(response.url, self.webUrl + '/wp-content/uploads/2014/11/' + file_name)
		print 'file id: ' + response.id

	def test_upload_feature_image(self):
		self.assertIsInstance(postEngine.uploadFeatureImage('AS104'), (int,long))

	def test_upload_product_image(self):
		self.assertIsInstance(postEngine.uploadProductImage(), array)


	def test_post(self):
		self.assertTrue(self.doer.post())



def main():
	unittest.main()


if __name__ == '__main__':
	main()