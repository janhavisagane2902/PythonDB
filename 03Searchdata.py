import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='290200',database='bookstoredb')
curs=con.cursor()

bcd=int(input('Enter bookcode '))

curs.execute("select booknm,category,author,price from books where bookcode=%s"%bcd)
rec=curs.fetchone()

try:
    print('Book name is:%s'%rec[0])
    print('Category:%s'%rec[1])
    print('author:%s'%rec[2])
    print('price of book is:%.2f'%rec[3])
except:
    print('Book not find...')

con.close()