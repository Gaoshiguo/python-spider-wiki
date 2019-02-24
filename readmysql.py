import pymysql.cursors
#建立数据库连接
connection = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    db = "wikiurl",
    charset = "utf8mb4")
try:
    #获取回话指针
    with connection.cursor() as cursor:
        #写SQL语句
        sql = "select `urlname`,`urlhref` from `urls` where `id`is not null "
        num = cursor.execute(sql)
        #打印输出所有满足条件的数目
        print(num)
        result = cursor.fetchall()
        #打印输出所有满足条件的连接
        print(result)
        #打印输出前三条
        result_2 = cursor.fetchmany(size = 3)
        print(result_2)

finally:
    #关闭连接
    connection.close()