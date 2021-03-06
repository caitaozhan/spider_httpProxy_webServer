import re
import urllib2
import meizi_series_getpage


def loadurl(url):
	try:
		conn = urllib2.urlopen(url, timeout=5)
		html = conn.read()
		return html
	except urllib2.URLError:
		return ""

def printList(list):
	print("[")
	for i in list:
		print(i)
	print("]\n")


def nextpage(url, path):
	reNextLink = "<a.*?href='(.*?)'>.*?</a>"
	reNextPage = '<div.*?id="wp_page_number.*?>.*?<ul>(.*?)</ul>'
	searchPathTail = ".*/([a-z]+).*?.html"
	searchurltail = ".*/(.*?.html)"
	searchhead = "(.*)/.*?.html"
	pathTail = re.findall(searchPathTail, url, re.S)
	urlTail = re.findall(searchurltail, url, re.S)
	urlhead = re.findall(searchhead, url, re.S)
	path = path + '/' + pathTail[0]
	nextpageurl = []
	html = ""
	while True:
		html = loadurl(url)
		if html == "":
			print("load" + url + "error")
			continue
		else:
			break
	nextPage = re.findall(reNextPage, html, re.S)
	nextLink = re.findall(reNextLink, nextPage[0], re.S)
	nextLink.append(urlTail[0])
	nextLink = sorted(list(set(nextLink)))
	for i in nextLink:
		nextpageurl.append(urlhead[0] + "/" + i)
	for i in nextpageurl:
		print(i)
		meizi_series_getpage.tag_series(i, path)


if __name__ == "__main__":
	nextpage("http://www.meizitu.com/a/sifang.html", "/home/shiyanlou/Desktop/demo454")

