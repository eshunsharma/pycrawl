from HTMLParser import HTMLParser
from urlparse import urljoin

class LinkFinder(HTMLParser):

	def __init__(self, base_url, page_url):
		HTMLParser.__init__(self)
		self.base_url = base_url
		self.page_url = page_url
		self.links = set()

	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			for (attribute, value) in attrs:
				if attribute == 'href':
					url = urljoin(self.base_url, value)
					self.links.add(url)
		if tag == 'img':
			for (attribute, value) in attrs:
				if attribute == 'src':
					url = urljoin(self.base_url, value)
					print(url)

	def page_links(self):
		return self.links

	def error(self, message):
		print('error ha: ' + message)