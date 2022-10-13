import pandas as pd
import mysql.connector
import datetime
from pyscrs.conf import *

timeNow = datetime.datetime.now()
crtMonth = timeNow.month
crtYear = timeNow.year

def addData(studentName, department, year, boardpoint, fee, paidfee, pendfee):
    con = mysql.connector.connect(host=DBHOST, user=DBUSERNAME, password=DBPASSWORD, database=DBNAME)
    cursor = con.cursor()
    qr = "INSERT INTO bus_fee_details_" + str(crtYear) + "_" + str(crtMonth) + " (Student_Name, Department, Year, Boarding_Point, Fee, Paid_Fee, Pending_Fee) VALUES (%s, %s, %s, %s, %s, %s, %s);"
    cursor.execute(qr, (studentName, department, year, boardpoint, fee, paidfee, pendfee))
    con.commit()

def deleteData(studentName, department, year, boardpoint, fee=None, paidfee=None, pendfee=None):
    con = mysql.connector.connect(host=DBHOST, user=DBUSERNAME, password=DBPASSWORD, database=DBNAME)
    cursor = con.cursor()
    qr = "DELETE FROM bus_fee_details_" + str(crtYear) + "_" + str(crtMonth) + " WHERE Student_Name='" + studentName + "' AND Department='" + department + "' AND Year='"+year+"' AND Boarding_Point='" + boardpoint + "';"
    cursor.execute(qr)
    con.commit()

def editData(studentName, department, year, boardpoint, fee, pendfee, oldstud, olddept, oldyear):
    con = mysql.connector.connect(host=DBHOST, user=DBUSERNAME, password=DBPASSWORD, database=DBNAME)
    cursor = con.cursor()
    qr = "UPDATE bus_fee_details_" + str(crtYear) + "_" + str(crtMonth) + " SET  Student_Name=%s, Department=%s, Year=%s, Boarding_Point=%s, Fee=%s, Pending_Fee=%s WHERE Student_Name=%s AND Department=%s AND Year=%s;"

    cursor.execute(qr, (studentName, department, year, boardpoint, fee, pendfee, oldstud, olddept, oldyear))
    con.commit()