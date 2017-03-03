import urllib2
import urllib

url = 'https://www.zhihu.com/topic'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)','Referer':'https://www.zhihu.com/topic'}
request = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(request)
print response.read()
# try:
# 	response = urllib2.urlopen(request)
# except urllib2.HTTPError,e:
# 	print e.code
# except urllib2.URLError,e:
# 	print e.reason
# else:
# 	print 'OK'

# print response.read()