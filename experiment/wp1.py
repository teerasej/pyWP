from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo

wp = Client('http://localhost:8888/trakulthai/xmlrpc.php', 'admin', '12345')
wp.call(GetPosts());