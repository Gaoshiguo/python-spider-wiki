import urllib
import urllib.request
url = "www.baidu.com"
req = urllib.request.urlopen(url)
content = req.read().decode("utf-8")
print(content)