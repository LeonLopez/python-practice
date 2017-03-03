 # -*- coding: utf-8 -*-
import urllib2
import urllib
import cookielib

filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
data = urllib.urlencode({'account':'3114005899','password':'GMZ14035899'})
url = 'http://222.200.98.147/'
headers  = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)','Referer':'http://222.200.98.147/'}
request = urllib2.Request(url,data,headers)
try:
	response = opener.open(request)
except urllib2.HTTPError,e:
	print e.code
except urllib2.URLError,e:
	print e.reason

cookie.save(ignore_discard=True,ignore_expires=True)
eduurl = 'http://222.200.98.147/login!welcome.action'
result = opener.open(eduurl)
print result.read()
