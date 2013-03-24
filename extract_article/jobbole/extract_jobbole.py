from pyquery import PyQuery
from lxml import etree


url_handle = PyQuery("http://blog.jobbole.com/tag/python/") 
article_title = url_handle('.meta-title').text()
print article_title
