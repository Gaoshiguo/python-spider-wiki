import urllib
import urllib.request
url = "http://www.sina.com"
user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
req = urllib.request.Request(url,headers={user_agent:'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.13'})
res = urllib.request.urlopen(req)
res = res.read().decode("utf-8")
print(res)