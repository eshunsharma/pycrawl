from urlparse import urlparse

# Get domain name (domain.com)

def get_domain(url):
	try:
		results = get_subdomain(url).split('.')
		print(results)
		return results[-2] + '.' + results[-1]
	except:
		return ''

# Get subdomain/domain (sub.domain.com)

def get_subdomain(url):
	try:
		return urlparse(url).netloc
	except:
		return ''