import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='290200',database='bookstoredb')
curs=con.cursor()

auth=input("Enter the author of the book: ")
curs.execute("select * from books where author='%s'"%(auth))
rec=curs.fetchone()


publ=input("Enter the publication: ")
curs.execute("select * from books where publication='%s'"%(publ))
rec=curs.fetchone()

if rec:
    print(rec[1])
else:
    print('Book not found..')
con.close()



