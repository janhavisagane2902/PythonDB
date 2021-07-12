import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='290200',database='bookstoredb')
curs=con.cursor()

bcd=int(input("Enter the bookcode you want to delete "))

curs.execute("select * from books where bookcode=%d"%bcd)
rec=curs.fetchone()

try:
    print("bookcode : %d"%rec[0])
    print("bookname : %s"%rec[1])
    print("category : %s"%rec[2])
    print("author : %s"%rec[3])
    print("publication : %s"%rec[4])
    print("edition : %s"%rec[5])
    print("price : %s"%rec[6])

    curs.execute("delete from books where bookcode=%d"%bcd)
    bcd=input('Do you want to continue?')
    while bcd.upper()=='YES':
        print('Book deleted successfully')
        con.commit()

except:
    print("book does not exists")
