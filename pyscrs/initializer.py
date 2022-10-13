import datetime
import mysql.connector
import pandas as pd
from pyscrs.conf import *



def createNewTableCont(tableNow):
    timenow = datetime.datetime.now()
    monthnow = timenow.month
    yearnow = timenow.year
    con = mysql.connector.connect(host=DBHOST, user=DBUSERNAME, password=DBPASSWORD, database=DBNAME)
    cursor = con.cursor()
    cursor.execute("SELECT * FROM " + tableNow)
    allDatas = cursor.fetchall()
    allData = pd.DataFrame(allDatas, columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
    StudentName = allData["Student Names"]
    Departments = allData["Department"]
    Years = list(allData["Year"])
    BoardingPoint = allData["Boarding Point"]
    TotalFee = list(allData["Fee"])
    PaidFee = []
    PendingFee = []
    for i in range(0, len(StudentName)):
        PaidFee.append(0)
        PendingFee.append(TotalFee[i])
    for i in range(0, len(StudentName)):
        quert = "INSERT INTO bus_fee_details_" + str(yearnow) + "_" + str(monthnow) +" (Student_Name, Department, Year, Boarding_Point, Fee, Paid_Fee, Pending_Fee) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(quert, (StudentName[i], Departments[i], Years[i], BoardingPoint[i], TotalFee[i], PaidFee[i], PendingFee[i]))
    con.commit()


def initialize():
    timenow = datetime.datetime.now()
    monthnow = timenow.month
    yearnow = timenow.year
    
    con = mysql.connector.connect(host=DBHOST, user=DBUSERNAME, password=DBPASSWORD, database=DBNAME)
    cursor = con.cursor(buffered=True)
    
    # Create a new table if not exists

    qry = "CREATE TABLE if not exists bus_fee_details_" + str(yearnow) + "_" + str(monthnow) + " (Student_Name varchar(100), Department varchar(50), Year int, Boarding_Point varchar(200), Fee int, Paid_Fee int, Pending_Fee int);"
    result = cursor.execute(qry)
    print(result)
    con.commit()

    qry = "SELECT * from bus_fee_details_" + str(yearnow) + "_" + str(monthnow)
    cursor.execute(qry)

    fetchResult = cursor.fetchone()
    try:
        print(fetchResult[0])

    except Exception:
        if monthnow == 1:
            qry = "SELECT COUNT(*) FROM information_schema.tables WHERE table_name='bus_fee_details_"+ str(yearnow-1) +"_" + str(12) + "';"
            cursor.execute(qry)
            tableCounts = cursor.fetchone()[0]
            if tableCounts == 1:
                createNewTableCont("bus_fee_details_"+ str(yearnow-1) +"_" + str(12))
        else:
            qry = "SELECT COUNT(*) FROM information_schema.tables WHERE table_name='bus_fee_details_"+ str(yearnow) +"_" + str(monthnow-1) + "';"

            cursor.execute(qry)
            tableCounts = cursor.fetchone()[0]
            if tableCounts == 1:
                createNewTableCont("bus_fee_details_"+ str(yearnow) +"_" + str(monthnow-1))
    
