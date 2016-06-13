#!/usr/bin/env python

import re
import urllib2
import meizi_series_nextpage


def loadurl(url):
	try:
		conn = urllib2.urlopen(url, data=None, timeout=5)
		html = conn.read()
		return html
	except Exception:
		return ""


def meizi(url, path):
	reTagContent = '<div.*?class="tags">.*?<span>(.*?)</span>'
	reTagUrl = '<a.*?href="(.*?)".*?>'
	print("start open meiziwang")
	html = ""
	while True:
		html = loadurl(url)
		if html == "":
			print("load " + url + "error")
			continue
		else:
			break
	tagContent = re.findall(reTagContent, html, re.S)
	taglists = re.findall(reTagUrl, tagContent[0], re.S)
	taglists = sorted(list(set(taglists)))
	for url in taglists:
		meizi_series_nextpage.nextpage(url, path)

print("hehe")
if __name__ == "__main__":
	print("Spider start!")
	meizi("http://www.meizitu.com", "/home/shiyanlou/Desktop/meizi")
	print("Spider Stop~")

