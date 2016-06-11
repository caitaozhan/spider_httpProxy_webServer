import urllib2
import os
import re

def loadurl(url):
	try:
		conn = urllib2.urlopen(url, timeout=5)
		html = conn.read()
		return html
	except urllib2.URLError:
		return ""


def download(url, filename):
	try:
		conn = urllib2.urlopen(url, timeout=5)
		f = open(filename, "wb")
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
	print(filename + ": start")
	while True:
		if os.path.exists(filename):
			print(filename + " exists, skip")
			return True
		elif os.path.exists(filename):
			os.mknod(filename)
		if download(url, filename):
			break
	print(filename + ": over")


def pic_list(picList, path):
	picurl = ""
	for picurl in picList:
		save_pic(picurl, path)


def picurl(url, path):
	if os.path.exists(path):
		print(path + "exist")
	else:
		os.makedirs(path)
	html = ""
	while True:
		html = loadurl(url)
		if html == "":
			print("load" + url + "error")
			continue
		else:
			break
	rePicContent1 = '<div.*?id="picture.*?>.*?<p>(.*?)</p>'
	rePicContent2 = '<div.*?class="postContent.*?>.*?<p>(.*?)</p>'
	rePicList = '<img.*?src="(.*?)".*?>'
	picContent = re.findall(rePicContent1, html, re.S)
	if len(picContent) <= 0:
		picContent = re.findall(rePicContent2, html, re.S)
	if len(picContent) <= 0:
		print("load false, over download this page and return")
		return False
	else:
		print(picContent)
		picList = re.findall(rePicList, picContent[0], re.S)
		print(picList)
		pic_list(picList, path)


if __name__ == "__main__":
	url = "http://www.meizitu.com/a/454.html"
	picurl(url, "/home/shiyanlou/Desktop/demo454")


