# python-spider-wiki
这个项目使用python来实现爬取维基百科的关键词条以及其超链接，并写入MySQL数据库中
使用Python实现的爬虫代码，爬取维基百科词条及网址，以及运行截图 一、我们使用的python版本是python3.6，使用的开发工具是pycharm， 使用到的包有request、beautifulsoup、pysql，使用了mysql数据库。 为了方便数据的查询，我们还使用了一种免费的小型的可视化数据库软件来连接数据库，该软件为Navicat Premium

![image](https://github.com/Gaoshiguo/python-spider-wiki/blob/master/%E6%88%AA%E5%9B%BE/1.png)

二、项目初期，我们先进行一个简单的爬虫练习。我们先使用request对简单的网址进行爬取数据，由易到难 spider-test.py文件时最开始较简单的爬取慕课网主页面的HTML文档，爬取的HTML文档如下图所示

![image](https://github.com/Gaoshiguo/python-spider-wiki/blob/master/%E6%88%AA%E5%9B%BE/2.png)

三、在此基础上，我们通过使用beautifulsoup来分析爬取到的HTML文档，进行进一步的数据采集，运行testday_3.py代码后的结果如下图所示：

![image](https://github.com/Gaoshiguo/python-spider-wiki/blob/master/%E6%88%AA%E5%9B%BE/3.png)

四、由于我们使用了MySQL数据库，所以必须有相应的代码来将爬到的数据写入数据库中，首先在数据库中建立相应的表单，如下图所示：

![image](https://github.com/Gaoshiguo/python-spider-wiki/blob/master/%E6%88%AA%E5%9B%BE/4.png)

如图所示，我们建立了名为urls的数据表，表中添加了两列属性，分别为urlname和urlhref，是我们这个项目要的“词条”和“超链接” 最终我们得到的爬虫数据在数据库的表单的展示为下图所示：

![image](https://github.com/Gaoshiguo/python-spider-wiki/blob/master/%E6%88%AA%E5%9B%BE/5.png)

![image](https://github.com/Gaoshiguo/python-spider-wiki/blob/master/%E6%88%AA%E5%9B%BE/6.png)

![image](https://github.com/Gaoshiguo/python-spider-wiki/blob/master/%E6%88%AA%E5%9B%BE/7.png)

最终我们在维基百科的主页面上爬取了555条数据，分别是页面上的词条和该词条所对应的超链接。
这个项目进一步的开发可以通过循环对每一条超链接跳转的页面爬取词条，然后再获取超链接，可以实现维基百科所有词条
的超链接的爬取，但是由于本人电脑设备有限，内存不足，实在不足以存储下如此海量的数据！
以此项目来练习python在爬虫方面上的强大功能。


