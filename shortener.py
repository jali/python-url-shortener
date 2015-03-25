#!/usr/bin/python

def base60encode(n):
	s = ""
	m = "0123456789ABCDEFGHJKLMNPQRSTUVWXYZ_abcdefghijkmnopqrstuvwxyz"
	if (n == 0):
		return 0
	while (n > 0):
		d = n % 60
		s = m[d] + s
		n = (n-d)/60
	return s

class Shortener(object):

	def __init__(self):
		self.id = 0
		self.urls = {}
	def shorten(self, url):
		self.id += 1
		token = base60encode(self.id)
		self.urls[token] = url
		return token

	def expand(self, token):
		return self.urls.get(token, None)

