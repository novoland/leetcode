import cookielib, urllib2
import re
import bs4

cookie = 'qa_noticed=1; __utma=217727755.2081047639.1393382282.1404960141.1404960141.1; __utmz=217727755.1404960141.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); csrftoken=E7JRlE2DuNO21ncHUgtijxoK2nGGUDcY; PHPSESSID=ammckrpu2x7djz6m6mmo7q8ioztcnhim; _ga=GA1.2.2081047639.1393382282'
def getCode(url,name):
	try:
		print 'getting file:'+name
		content = connect(url)
		txt = re.findall('scope.code.python = .*;',content)
		file_object = None
		if not txt:
			txt = re.findall('scope.code.java = .*;',content)
			file_object = open(name+'.java','wb')
		else:
			file_object = open(name+'.py','wb')
		txt = txt[0].split('=')[1]
		txt = txt[2:len(txt)-2]
		txt = txt.decode("unicode-escape")
		file_object.write(txt.encode('utf8'))
	except Exception, e:
		print 'error in file:'+name


def getlist():
	url = "https://oj.leetcode.com/problems/"
	content = bs4.BeautifulSoup(connect(url))
	frameurl = content.findAll(href=re.compile(r'/problems/.*/$'))
	for x in frameurl:		
		l = "https://oj.leetcode.com"+x['href']+"submissions/"
		name =  x['href'][10:len(x['href'])-1]				
		c = bs4.BeautifulSoup(connect(l))
		fra = c.findAll(href=re.compile(r'/submissions/detail/.*/$'))
		for y in fra:
			if 'Accepted' == y.find('strong').text:
				l = "https://oj.leetcode.com"+y['href']
				getCode(l,name)
				break
		

def connect(url):
	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	urllib2.install_opener(opener)
	req = urllib2.Request(url)
	req.add_header('Cookie', cookie)
	content = urllib2.urlopen(req).read()
	return content


if __name__ == '__main__':
	getlist()