import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='290200',database='bookstoredb')
curs=con.cursor()

try:
    bcd=int(input("enter book code "))

    curse.execute("select * from books where bookcode=%s"%bcd)
    rec=curs.fetchmany()

    if rec:
        bprc=int(intput("Enter New book price "))

        if bprc:
            curs.execute("update books set price=%d where bookcode=%s"%(bprc,bcd))
        else:
            print("Wrong Input Entered...")
        con.commit()
        print("New price updated successfully...")

        con.close()
    else:
        print("Bookk doesnot exist..")

except:
    print("Invalid input entered..")
