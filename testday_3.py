from bs4 import BeautifulSoup as bs
import re
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
soup = bs(html_doc,"html.parser")
print(soup.title.string)
for x in soup.find_all(re.compile("^b")):
    print(x.name)
#输出文档中所有的A标签中的href=HTTP://example.com/的网址
data = soup.find_all("a",href=re.compile("^http://example.com/"))
print(data)