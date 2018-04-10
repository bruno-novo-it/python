import pymysql

conn = pymysql.connect(host='172.20.0.2',user='root',password='', db='teste')

a = conn.cursor()

sql = 'SELECT * from tabela;'

a.execute(sql)

countrow = a.execute(sql)

print("Numberof Rows:", countrow)

data = a.fetchone()

print(data)
