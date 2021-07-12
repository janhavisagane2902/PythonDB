import mysql.connector as mycon 

con=mycon.connect(host='localhost',user='root',password='290200',database='bookstoredb')
curs=con.cursor()

curs.execute("select * from books")

while True:
    data=curs.fetchmany(5)
    if not data:
        break
    print(data)

    con.close()