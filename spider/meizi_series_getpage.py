import re
import urllib2
import meizi_page_download


def loadurl(url):
	try:
		conn = urllib2.urlopen(url, timeout=5)
		html = conn.read()
		return html
	except urllib2.URLError:
		return ""
	except Exception:
		print("unkown exception in conn.read()")
		return ""

def oneOfSeries(urllist, path):
	searchname = ".*/(.*?).html"
	current_path = ""
	for url in urllist:
		try:
			name = re.findall(searchname, url, re.S)
			current_path = path + '/' + name[0]
			meizi_page_download.picurl(url, current_path)
		except urllib2.URLError:
			pass


def printList(list):
	print("[")
	for i in list:
		print(i)
	print("]\n")


def tag_series(url, path):
	reSeriesList = '<div.*?class="pic".*?>.*?<a.*?href="(.*?)".*?target.*?>'
	html = ""
	while True:
		html = loadurl(url)
		if html == "":
			print("load" + url + "error")
			continue
		else:
			break
	seriesList = re.findall(reSeriesList, html, re.S)
	if len(seriesList) == 0:
		pass
	else:	
		oneOfSeries(seriesList, path)

