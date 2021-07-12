import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='290200',database='bookstoredb')
curs=con.cursor()

try:
    bookcd=int(input('Enter bookcode '))
    booknm=input('Enter name of the Book ')
    cat=input('Enter category ')
    auth=input('Enter author ')
    publ=int(input('Enter publication date '))
    edi=input('Enter edition ')
    prc=float(input('Enter price of book '))

    curs.execute("insert into books values(%d,'%s','%s','%s',%d,'%s',%.2f)"%(bookcd,booknm,cat,auth,publ,edi,prc))
    con.commit()

    print('Books inserted into databse successfully!!')



except:
    print('Error Inserting data..')

con.close()