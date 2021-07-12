import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='290200',database='bookstoredb')
curs=con.cursor

curs.execute("select * from books where category='autobiography'")
data=curs.fetchall()
print(type(data))
print(data)

for rec in data:
    print(rec)
    print(rec[1])

con.close()