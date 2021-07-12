import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='290200',database='bookstoredb')
curs=mycon.cursor()

bcd=int(input("Enter the bookcode "))
rw=input("Enter the review  ")
try:
    curs.execute("update books set review=%s where bookcode=%d"%(rw,bcd))
    con.commit()

except:
    print("Invalid input entered...")