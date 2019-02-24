from bs4 import BeautifulSoup as bs
#这部分为名为HTML——doc的一个HTML文件
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
#一直到这里都是HTML文件
#soup 实例化，括号中有两个参数，一个为HTML文档名，另一个为所使用的解析器
soup = bs(html_doc,"html.parser")
#格式化打印输出文档
print(soup.prettify())
#打印输出文档中所有的a标签
print(soup.find_all('a'))
#打印输出文档中所有的文字
print(soup.get_text())
#打印输出文档中的第一个P标签
print(soup.p)
#打印输出文档中所有的id为link3的标签
print(soup.find(id="link3"))
#打印输出文档的title
print(soup.title)
#只打印输出文档的title字符串不输出格式符
print(soup.title.string)
#打印输出title 的name
print(soup.title.name)
#从文档中找到所有<a>标签的链接
for link in soup.find_all('a'):
    print(link.get('herf'))