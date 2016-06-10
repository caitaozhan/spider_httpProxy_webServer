import urllib2
import os
import re

def loadurl(url):
	try:
		conn = urllib2.urlopen(url, timeout=5)
		html = conn.read()
		return html
	except urllib2.URLError:
		return ''


def download(url, filename):
	try:
		conn = urllib2.urlopen(url, timeout=5)
		f = open(filename, 'wb')
		f.write(conn.read())
		f.close()
		return True
	except urllib2.URLError:
		print("load" + url + "error")
		return False


def save_pic(url, path):
	searchname = ".*/(.*?.jpg)"
	name = re.findall(searchname, url)
	filename = path + '/' + name[0]
	print(filename + ":start")
	while True:
		if os.path.exists(filename):
			
