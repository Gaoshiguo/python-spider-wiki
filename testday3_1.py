from bs4 import BeautifulSoup as bs
import re
#为HTML文档设置名称html_doc
html_doc="""
 <html>
  <head>
  <title>
    The Dormouse's story
  </title>
 </head>
 <body>
   <p class="title">
    <b>
     The Dormouse's story
    </b>
   </p>
   <p class="story">
    Once upon a time there were three little sisters; and their names were
    <a class="sister" href="http://example.com/elsie" id="link1">
     Elsie
    </a>
    ,
    <a class="sister" href="http://example.com/lacie" id="link2">
     Lacie
    </a>
    and
    <a class="sister" href="http://example.com/tillie" id="link2">
     Tillie
    </a>
    ; and they lived at the bottom of a well.
   </p>
   <p class="story">
    ...
   </p>
  </body>
 </html>

"""
#将soup对象实例化,第一个参数为HTML文档名，第二个参数为文档解析器
soup = bs(html_doc,"html.parser")
#格式化输出HTML文档对象
#打印输出文档中所有的ID为link1的标签，因为标签是以列表的形式出现的，所以不能直接获取标签的
#内容，而是通过遍历每一个对象，在获取对象的String
#print(soup.find(id='link2').get_text())
#for x in soup.find_all(id="link1"):
   # print(x.String)
print(soup.find_all("a"))
for x in soup.find_all("a"):
    print(x.string)
#当我们想查找class为story的标签时，不能直接使用find（class=“story”）
#因为class是一个关键字，我们需要进行如下处理，传入一个参数p，代表的是
#从p标签中查找，再用一个花括号传入两个参数用冒号隔开，代表class为story
print(soup.find("p",{"class":"story"}))
#使用正则表达式来查找标签
#查找出文档中所有的以b开头的标签，然后输出这些标签的name
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
#查找a标签中所有的以http://example.com/为前缀，后面内容任意网址的标签
data = soup.findAll("a",href=re.compile(r"^http://example\.com/"))
print(data)