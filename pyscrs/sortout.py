import pandas as pd
import mysql.connector
import datetime
from pyscrs.conf import *
import os

def getNotPaidInfo():
    curTime = datetime.datetime.now()
    crYear = curTime.year
    crMonth = curTime.month
    con = mysql.connector.connect(host=DBHOST, user=DBUSERNAME, password=DBPASSWORD, database=DBNAME)

    previousData1 = ""
    previousData2 = ""
    previousData3 = ""
    previousData4 = ""

    cursor = con.cursor()
    if crMonth == 1:
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            currentMonthData = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear-1) + "_" + str(12) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # dec = cursor.fetchall()[0][0]
            previousData1 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear-1) + "_" + str(11) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # nov = cursor.fetchall()[0][0]
            previousData2 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear-1) + "_" + str(10) +" WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # oct = cursor.fetchall()[0][0]
            previousData3 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear-1) + "_" + str(9) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # sep = cursor.fetchall()[0][0]
            previousData4 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        # totalPending = jan+feb+mar+apr+may+jun+jul+aug+sep+oct+nov+dec


        # For Month 2
    elif crMonth == 2:
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # feb = cursor.fetchall()[0][0]
            currentMonthData = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-1) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # jan = cursor.fetchall()[0][0]
            previousData1 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear-1) + "_" + str(12) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # dec = cursor.fetchall()[0][0]
            previousData2 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear-1) + "_" + str(11) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # nov = cursor.fetchall()[0][0]
            previousData3 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear-1) + "_" + str(10) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # oct = cursor.fetchall()[0][0]
            previousData4 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        # totalPending = jan+feb+mar+apr+may+jun+jul+aug+sep+oct+nov+dec


    # For Month 3
    elif crMonth == 3:
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # mar = cursor.fetchall()[0][0]
            currentMonthData = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-1) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # feb = cursor.fetchall()[0][0]
            previousData1 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-2) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # jan = cursor.fetchall()[0][0]
            previousData2 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear-1) + "_" + str(12) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # dec = cursor.fetchall()[0][0]
            previousData3 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear-1) + "_" + str(11) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # nov = cursor.fetchall()[0][0]
            previousData4 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        # totalPending = jan+feb+mar+apr+may+jun+jul+aug+sep+oct+nov+dec


    # For Month 4
    elif crMonth == 4:
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # apr = cursor.fetchall()[0][0]
            currentMonthData = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-1) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # mar = cursor.fetchall()[0][0]
            previousData1 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-2) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # feb = cursor.fetchall()[0][0]
            previousData2 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-3) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # jan = cursor.fetchall()[0][0]
            previousData3 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear-1) + "_" + str(12) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # dec = cursor.fetchall()[0][0]
            previousData4 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        # totalPending = jan+feb+mar+apr+may+jun+jul+aug+sep+oct+nov+dec

    # For Month 5
    elif crMonth == 5:
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # may = cursor.fetchall()[0][0]
            currentMonthData = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-1) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # apr = cursor.fetchall()[0][0]
            previousData1 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-2) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # mar = cursor.fetchall()[0][0]
            previousData2 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-3) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # feb = cursor.fetchall()[0][0]
            previousData3 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-4) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # jan = cursor.fetchall()[0][0]
            previousData4 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass

        # totalPending = jan+feb+mar+apr+may+jun+jul+aug+sep+oct+nov+dec
    
    # For Month 6
    elif crMonth == 6:
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # jun = cursor.fetchall()[0][0]
            currentMonthData = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-1) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # may = cursor.fetchall()[0][0]
            previousData1 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-2) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # apr = cursor.fetchall()[0][0]
            previousData2 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-3) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # mar = cursor.fetchall()[0][0]
            previousData3 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-4) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # feb = cursor.fetchall()[0][0]
            previousData4 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass

        # totalPending = jan+feb+mar+apr+may+jun+jul+aug+sep+oct+nov+dec
    
    # For Month 7
    elif crMonth == 7:
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # jul = cursor.fetchall()[0][0]
            currentMonthData = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-1) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # jun = cursor.fetchall()[0][0]
            previousData1 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-2) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # may = cursor.fetchall()[0][0]
            previousData2 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-3) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # apr = cursor.fetchall()[0][0]
            previousData3 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-4) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # mar = cursor.fetchall()[0][0]
            previousData4 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        # totalPending = jan+feb+mar+apr+may+jun+jul+aug+sep+oct+nov+dec

    # For Month 8
    elif crMonth == 8:
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # aug = cursor.fetchall()[0][0]
            currentMonthData = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
            
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-1) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # jul = cursor.fetchall()[0][0]
            previousData1 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-2) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # jun = cursor.fetchall()[0][0]
            previousData2 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-3) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # may = cursor.fetchall()[0][0]
            previousData3 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-4) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # apr = cursor.fetchall()[0][0]
            previousData4 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        # totalPending = jan+feb+mar+apr+may+jun+jul+aug+sep+oct+nov+dec
    
    # For Month 9
    elif crMonth == 9:
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # sep = cursor.fetchall()[0][0]
            currentMonthData = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-1) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # aug = cursor.fetchall()[0][0]
            previousData1 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-2) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # jul = cursor.fetchall()[0][0]
            previousData2 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-3) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # jun = cursor.fetchall()[0][0]
            previousData3 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-4) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # may = cursor.fetchall()[0][0]
            previousData4 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        # totalPending = jan+feb+mar+apr+may+jun+jul+aug+sep+oct+nov+dec

    # For Month 10
    elif crMonth == 10:
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # oct = cursor.fetchall()[0][0]
            currentMonthData = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-1) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # sep = cursor.fetchall()[0][0]
            previousData1 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-2) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # aug = cursor.fetchall()[0][0]
            previousData2 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-3) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # jul = cursor.fetchall()[0][0]
            previousData3 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-4) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # jun = cursor.fetchall()[0][0]
            previousData4 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        # totalPending = jan+feb+mar+apr+may+jun+jul+aug+sep+oct+nov+dec
    
    # For Month 11
    elif crMonth == 11:
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # nov = cursor.fetchall()[0][0]
            currentMonthData = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-1) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # oct = cursor.fetchall()[0][0]
            previousData1 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-2) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # sep = cursor.fetchall()[0][0]
            previousData2 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-3) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # aug = cursor.fetchall()[0][0]
            previousData3 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-4) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # jul = cursor.fetchall()[0][0]
            previousData4 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        # totalPending = jan+feb+mar+apr+may+jun+jul+aug+sep+oct+nov+dec
    
    # For Month 12
    elif crMonth == 12:
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # dec = cursor.fetchall()[0][0]
            currentMonthData = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-1) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # nov = cursor.fetchall()[0][0]
            previousData1 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-2) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # oct = cursor.fetchall()[0][0]
            previousData2 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT * FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-3) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # sep = cursor.fetchall()[0][0]
            previousData3 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-4) + " WHERE Pending_Fee!=0"
            cursor.execute(qry)
            # aug = cursor.fetchall()[0][0]
            previousData4 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
        except:
            pass

    return currentMonthData, previousData1, previousData2, previousData3, previousData4



def exportOverviewData(currentMonthData, previousData1, previousData2, previousData3, previousData4):
    crMonth = datetime.datetime.now().month
    crYear = datetime.datetime.now().year
    crDay = datetime.datetime.now().day
    crHour = datetime.datetime.now().hour
    crMinute = datetime.datetime.now().minute
    crSecond = datetime.datetime.now().second
    
    neededFolder = "exportedData/" + str(crDay) + "-" + str(crMonth) + "-" + str(crYear) + "/"

    # Check or Create a folder

    isExists = os.path.exists(neededFolder)
    if isExists == False:
        os.mkdir(neededFolder)
    else:
        pass

    ## For Current Month

    if len(currentMonthData) != 0:
        deparments = currentMonthData["Department"].unique()
        for depts in deparments:
            print(depts)
            notPaidAkDept = currentMonthData[currentMonthData["Department"] == depts]
            notPaidAkDept.to_excel(neededFolder + str(depts) + "-" + str(crHour) + "-" + str(crMinute) + "-" + str(crSecond) + ".xlsx", index=False)

    ## For Previous Month

    if len(previousData1) != 0:
    
        deparments = previousData1["Department"].unique()
        for depts in deparments:
            notPaidAkDept = previousData1[previousData1["Department"] == depts]
            notPaidAkDept.to_excel(neededFolder + str(depts) + "-" + str(crHour) + "-" + str(crMinute) + "-" + str(crSecond) + ".xlsx", index=False)
        
    ## Previous Data 2

    if len(previousData2) != 0:
    
        deparments = previousData2["Department"].unique()
        for depts in deparments:
            notPaidAkDept = previousData2[previousData2["Department"] == depts]
            notPaidAkDept.to_excel(neededFolder + str(depts) + "-" + str(crHour) + "-" + str(crMinute) + "-" + str(crSecond) + ".xlsx", index=False)

    ## Previous Data 3

    if len(previousData3) != 0:
    
        deparments = previousData3["Department"].unique()
        for depts in deparments:
            notPaidAkDept = previousData3[previousData3["Department"] == depts]
            notPaidAkDept.to_excel(neededFolder + str(depts) + "-" + str(crHour) + "-" + str(crMinute) + "-" + str(crSecond) + ".xlsx", index=False)

    ## Previous Data 4

    if len(previousData4) != 0:
    
        deparments = previousData4["Department"].unique()
        for depts in deparments:
            notPaidAkDept = previousData4[previousData4["Department"] == depts]
            notPaidAkDept.to_excel(neededFolder + str(depts) + "-" + str(crHour) + "-" + str(crMinute) + "-" + str(crSecond) + ".xlsx", index=False)