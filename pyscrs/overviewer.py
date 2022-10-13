import datetime
import mysql.connector
import pandas as pd
from pyscrs.conf import *

def getTotalNoOfStudents():
    curTime = datetime.datetime.now()
    crYear = curTime.year
    crMonth = curTime.month
    con = mysql.connector.connect(host=DBHOST, user=DBUSERNAME, password=DBPASSWORD, database=DBNAME)
    cursor = con.cursor()
    qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth)
    cursor.execute(qry)

    df = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
    return len(df)


def getTotalNumberOfNotPaid():
    curTime = datetime.datetime.now()
    crYear = curTime.year
    crMonth = curTime.month
    con = mysql.connector.connect(host=DBHOST, user=DBUSERNAME, password=DBPASSWORD, database=DBNAME)
    cursor = con.cursor()
    qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth)
    cursor.execute(qry)

    df = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
    notPaidInfo = len(df["Student Names"][df["Pending"] != 0])

    return notPaidInfo

def getTotalNoOfDepts():
    curTime = datetime.datetime.now()
    crYear = curTime.year
    crMonth = curTime.month
    con = mysql.connector.connect(host=DBHOST, user=DBUSERNAME, password=DBPASSWORD, database=DBNAME)
    cursor = con.cursor()
    qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth)
    cursor.execute(qry)

    df = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
    totalDepts = len(df["Department"].unique())

    return totalDepts


def getTotalNoOfStudentsInDepts():
    curTime = datetime.datetime.now()
    crYear = curTime.year
    crMonth = curTime.month
    con = mysql.connector.connect(host=DBHOST, user=DBUSERNAME, password=DBPASSWORD, database=DBNAME)
    cursor = con.cursor()
    qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth)
    cursor.execute(qry)

    df = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])


    return df["Department"].value_counts()


def getAllBoardingPoaints():
    curTime = datetime.datetime.now()
    crYear = curTime.year
    crMonth = curTime.month
    con = mysql.connector.connect(host=DBHOST, user=DBUSERNAME, password=DBPASSWORD, database=DBNAME)
    cursor = con.cursor()
    qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth)
    cursor.execute(qry)

    df = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])


    return df["Boarding Point"].value_counts()
