from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import re
#爬取维基百科主页面所有的词条信息对应的网址
#使用参数seq打开维基百科网页
seq = urlopen("https://en.wikipedia.org/wiki/Main_Page").read().decode("utf-8")
#使用参数soup对seq实例化
soup = bs(seq,"html.parser")
#打印输出文档，验证是否访问成功
#print(soup)
#通过观察文档可以发现，文档中的所有的词条都位于a标签中，并且前缀都是
#href="/wiki/"开头。所以我们使用正则表达式来进行词条的抓取
data = soup.findAll("a",href=re.compile("^/wiki/"))
for tag in data:
    #首次输出格式很乱。我们只需要输出标签中的
    #href属性就可以，所以我们通过遍历每一个data，
    #用tag来接收data的值，只输出其href属性
    #使用正则表达式删除了所有非网址文件
    #输出格式为第一个为词条的名字，中间用------隔开，后面的该词条的网址
    if not re.search("\.(jpg|JPG)$",tag["href"]):
        print(tag.get_text(),"------","https://en.wikipedia.org"+tag["href"])
    #通过观察输出对象我们发现有的是以/wiki/为开头的
    #但是结尾是.jpg或者.JPG很明显这类型的文件是一张图片
    #并非我们想要的网址
    #所以我们应该在限制一个条件来排除掉所有的非网址结果
