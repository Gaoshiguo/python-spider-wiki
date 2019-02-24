import pymysql.cursors
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import re
seq = urlopen("https://en.wikipedia.org/wiki/Main_Page").read().decode("utf-8")
soup = bs(seq,"html.parser")
data = soup.findAll("a",href=re.compile("^/wiki/"))
for tag in data:
    if not re.search("\.(jpg|JPG)$",tag["href"]):
        #print(tag.get_text(),"------","https://en.wikipedia.org"+tag["href"])
        #获取数据库连接
        connection = pymysql.connect(host = 'localhost',
                                     user = 'root',
                                     password = '123456',
                                     db = 'wikiurl',
                                     charset = 'utf8mb4'
                                     )
        try:
            #获取会话指针
            with connection.cursor() as cursor:
                #创建sql语句
                sql = "insert into `urls`(`urlname`,`urlhref`) values(%s,%s)"
                #执行sql语句
                cursor.execute(sql,(tag.get_text(),"https://en.wikipedia.org"+tag["href"]))
                #提交sql语句
                connection.commit()

        finally:
            connection.close()
#在使用python数据库时候，步骤如下：
#1.首先引入开发包：
#语句为：import pymysql.cursors
#2.获取数据库连接
#connection = pymysql.connect(host = 'localhost',
 #                                    user = 'root',
  #                                  db = 'wikiurl',
   #                                  charset = 'utf8mb4'
   #                                  )
#3.获取会话指针
#connection.cursors()
#4.执行sql语句
#cursors.excute(sql,(参数一，参数2，参数n))
#5.提交
#connection.commit()
#6.关闭
#connection.close()
#