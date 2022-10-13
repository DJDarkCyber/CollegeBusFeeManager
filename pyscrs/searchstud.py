import pandas as pd
import mysql.connector
import datetime
from pyscrs.conf import *

curtTime = datetime.datetime.now()
crMonth = curtTime.month
crYear  = curtTime.year


def searchit(studentName, month=None):
    con = mysql.connector.connect(host=DBHOST, user=DBUSERNAME, password=DBPASSWORD, database=DBNAME)
    # busdetails = pd.read_excel("data/studentFeeInfo/Bus-Fee-Data.xlsx", sheet_name=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    # foundStus = []
    # foundDepts = []
    # foundYear = []
    # foundBatch = []
    # foundTtlFee = []
    # foundPendFee = []
    # boardingPoint = []

    # for i in range(0, len(busdetails[0])):
    #     for x in range(0, len(busdetails)):
    #         if studentName.lower() in busdetails[x]["Student Name"][i].lower():
    #             foundStus.append(busdetails[x]["Student Name"][i])
    #             foundDepts.append(busdetails[x]["Department"][i])
    #             foundYear.append(busdetails[x]["Year"][i])
    #             foundBatch.append(busdetails[x]["Batch"][i])
    #             foundTtlFee.append(busdetails[x]["Total Fees"][i])
    #             boardingPoint.append(busdetails[x]["Boarding Point"][i])
    #             total_pending = 0
    #             for f in range(0, len(busdetails)):
    #                 total_pending += busdetails[f]["Pending Fees"][i]
    #             foundPendFee.append(total_pending) 
    #         break
    
    # return foundStus, foundDepts, foundYear, foundBatch, foundTtlFee, foundPendFee, boardingPoint


    # Data in Current Month 

    qry = "select * from bus_fee_details_" + str(crYear) + "_" + str(crMonth)  + " WHERE Student_Name LIKE \"%" + studentName + "%\";"
    cursor = con.cursor()
    cursor.execute(qry)
    currentMonthData = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])



    return currentMonthData["Student Names"], currentMonthData["Department"], currentMonthData["Year"], currentMonthData["Boarding Point"], currentMonthData["Fee"], currentMonthData["Pending"]


def displayInMonths(studentName):
    # busdetails = pd.read_excel("data/studentFeeInfo/Bus-Fee-Data.xlsx", sheet_name=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    # jan = busdetails[0]["Pending Fees"][ busdetails[0]["Student Name"] == studentName ]
    # feb = busdetails[1]["Pending Fees"][ busdetails[1]["Student Name"] == studentName ]
    # mar = busdetails[2]["Pending Fees"][ busdetails[2]["Student Name"] == studentName ]
    # apr = busdetails[3]["Pending Fees"][ busdetails[3]["Student Name"] == studentName ]
    # may = busdetails[4]["Pending Fees"][ busdetails[4]["Student Name"] == studentName ]
    # jun = busdetails[5]["Pending Fees"][ busdetails[5]["Student Name"] == studentName ]
    # jul = busdetails[6]["Pending Fees"][ busdetails[6]["Student Name"] == studentName ]
    # aug = busdetails[7]["Pending Fees"][ busdetails[7]["Student Name"] == studentName ]
    # sep = busdetails[8]["Pending Fees"][ busdetails[8]["Student Name"] == studentName ]
    # oct = busdetails[9]["Pending Fees"][ busdetails[9]["Student Name"] == studentName ]
    # nov = busdetails[10]["Pending Fees"][ busdetails[10]["Student Name"] == studentName ]
    # dec = busdetails[11]["Pending Fees"][ busdetails[11]["Student Name"] == studentName ]



    jan = feb = mar = apr = may = jun = jul = aug = sep = oct = nov = dec = 0

    allMonths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    calcMonths = [9, 10]

    con = mysql.connector.connect(host=DBHOST, user=DBUSERNAME, password=DBPASSWORD, database=DBNAME)
    # qry = "SELECT Pending_Fee FROM bus_fee_details_2022_9 WHERE Student_Name=\""+ studentName + "\""
    cursor = con.cursor()
    # Data in Current Month 

    qry = "select * from bus_fee_details_" + str(crYear) + "_" + str(crMonth)  + " WHERE Student_Name LIKE \"%" + studentName + "%\";"
    cursor = con.cursor()
    cursor.execute(qry)
    currentMonthData = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])

    # previousData1 = None
    # previousData2 = None
    # previousData3 = None
    # previousData4 = None

    # # Data in previous Month
    # if crMonth == 1:

    #     qry = "SELECT COUNT(*) FROM information_schema.tables WHERE table_name='bus_fee_details_"+ str(crYear-1) +"_" + str(12) + "'"

    #     cursor.execute(qry)
    #     tableCounts = cursor.fetchone()[0]

    #     if tableCounts == 1:
    #         qry =  "select Pending_Fee from bus_fee_details_" + str(crYear-1) + "_" + str(12)  + " WHERE Student_Name=\"" + studentName + "\";"
    #         cursor.execute(qry)
    #         previousData1 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
    # else:
    #     qry = "SELECT COUNT(*) FROM information_schema.tables WHERE table_name='bus_fee_details_"+ str(crYear) +"_" + str(crMonth-1) + "'"

    #     cursor.execute(qry)
    #     tableCounts = cursor.fetchone()[0]

    #     if tableCounts == 1:
    #         qry = "select Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(crMonth-1)  + " WHERE Student_Name=\"" + studentName + "\";"
    #         cursor.execute(qry)
    #         previousData1 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])


    # # Data in Previous Month
    # if crMonth == 1:
    #     qry = "SELECT COUNT(*) FROM information_schema.tables WHERE table_name='bus_fee_details_"+ str(crYear-1) +"_" + str(11) + "'"

    #     cursor.execute(qry)
    #     tableCounts = cursor.fetchone()[0]

    #     if tableCounts == 1:
    #         qry = "select Pending_Fee from bus_fee_details_" + str(crYear-1) + "_" + str(11)  + " WHERE Student_Name=\"" + studentName + "\";"
    #         cursor.execute(qry)
    #         previousData2 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
    # elif crMonth == 2:
    #     qry = "SELECT COUNT(*) FROM information_schema.tables WHERE table_name='bus_fee_details_"+ str(crYear-1) +"_" + str(12) + "'"

    #     cursor.execute(qry)
    #     tableCounts = cursor.fetchone()[0]

    #     if tableCounts == 1:
    #         qry = "select Pending_Fee from bus_fee_details_" + str(crYear-1) + "_" + str(12)  + " WHERE Student_Name=\"" + studentName + "\";"
    #         cursor.execute(qry)
    #         previousData2 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
    # else:
    #     qry = "SELECT COUNT(*) FROM information_schema.tables WHERE table_name='bus_fee_details_"+ str(crYear) +"_" + str(crMonth-2) + "'"

    #     cursor.execute(qry)
    #     tableCounts = cursor.fetchone()[0]

    #     if tableCounts == 1:
    #         qry = "select Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(crMonth-2)  + " WHERE Student_Name=\"" + studentName + "\";"
    #         cursor.execute(qry)
    #         previousData2 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])

    # # Data in Previous Month

    # if crMonth == 1:
    #     qry = "SELECT COUNT(*) FROM information_schema.tables WHERE table_name='bus_fee_details_"+ str(crYear-1) +"_" + str(10) + "'"

    #     cursor.execute(qry)
    #     tableCounts = cursor.fetchone()[0]

    #     if tableCounts == 1:
    #         qry = "select Pending_Fee from bus_fee_details_" + str(crYear-1) + "_" + str(10)  + " WHERE Student_Name=\"" + studentName + "\";"
    #         cursor.execute(qry)
    #         previousData3 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
    # elif crMonth == 2:
    #     qry = "SELECT COUNT(*) FROM information_schema.tables WHERE table_name='bus_fee_details_"+ str(crYear-1) +"_" + str(11) + "'"

    #     cursor.execute(qry)
    #     tableCounts = cursor.fetchone()[0]

    #     if tableCounts == 1:
    #         qry = "select Pending_Fee from bus_fee_details_" + str(crYear-1) + "_" + str(11)  + " WHERE Student_Name=\"" + studentName + "\";"
    #         cursor.execute(qry)
    #         previousData3 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
    # elif crMonth == 3:
    #     qry = "SELECT COUNT(*) FROM information_schema.tables WHERE table_name='bus_fee_details_"+ str(crYear-1) +"_" + str(12) + "'"

    #     cursor.execute(qry)
    #     tableCounts = cursor.fetchone()[0]

    #     if tableCounts == 1:
    #         qry = "select Pending_Fee from bus_fee_details_" + str(crYear-1) + "_" + str(12)  + " WHERE Student_Name=\"" + studentName + "\";"
    #         cursor.execute(qry)
    #         previousData3 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
    # else:
    #     qry = "SELECT COUNT(*) FROM information_schema.tables WHERE table_name='bus_fee_details_"+ str(crYear) +"_" + str(crMonth-3) + "'"

    #     cursor.execute(qry)
    #     tableCounts = cursor.fetchone()[0]

    #     if tableCounts == 1:
    #         qry = "select Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(crMonth-3)  + " WHERE Student_Name=\"" + studentName + "\";"
    #         cursor.execute(qry)
    #         previousData3 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])

    # # Data in Previous Month

    # if crMonth == 1:
    #     qry = "SELECT COUNT(*) FROM information_schema.tables WHERE table_name='bus_fee_details_"+ str(crYear-1) +"_" + str(9) + "'"

    #     cursor.execute(qry)
    #     tableCounts = cursor.fetchone()[0]

    #     if tableCounts == 1:
    #         qry = "select Pending_Fee from bus_fee_details_" + str(crYear-1) + "_" + str(9)  + " WHERE Student_Name=\"" + studentName + "\";"
    #         cursor.execute(qry)
    #         previousData4 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
    # elif crMonth == 2:
    #     qry = "SELECT COUNT(*) FROM information_schema.tables WHERE table_name='bus_fee_details_"+ str(crYear-1) +"_" + str(10) + "'"

    #     cursor.execute(qry)
    #     tableCounts = cursor.fetchone()[0]

    #     if tableCounts == 1:
    #         qry = "select Pending_Fee from bus_fee_details_" + str(crYear-1) + "_" + str(10)  + " WHERE Student_Name=\"" + studentName + "\";"
    #         cursor.execute(qry)
    #         previousData4 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
    # elif crMonth == 3:
    #     qry = "SELECT COUNT(*) FROM information_schema.tables WHERE table_name='bus_fee_details_"+ str(crYear-1) +"_" + str(11) + "'"

    #     cursor.execute(qry)
    #     tableCounts = cursor.fetchone()[0]

    #     if tableCounts == 1:
    #         qry = "select Pending_Fee from bus_fee_details_" + str(crYear-1) + "_" + str(11)  + " WHERE Student_Name=\"" + studentName + "\";"
    #         cursor.execute(qry)
    #         previousData4 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
    # elif crMonth == 4:
    #     qry = "SELECT COUNT(*) FROM information_schema.tables WHERE table_name='bus_fee_details_"+ str(crYear-1) +"_" + str(12) + "'"

    #     cursor.execute(qry)
    #     tableCounts = cursor.fetchone()[0]

    #     if tableCounts == 1:
    #         qry = "select Pending_Fee from bus_fee_details_" + str(crYear-1) + "_" + str(12)  + " WHERE Student_Name=\"" + studentName + "\";"
    #         cursor.execute(qry)
    #         previousData4 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
    # else:
    #     qry = "SELECT COUNT(*) FROM information_schema.tables WHERE table_name='bus_fee_details_"+ str(crYear) +"_" + str(crMonth-4) + "'"

    #     cursor.execute(qry)
    #     tableCounts = cursor.fetchone()[0]

    #     if tableCounts == 1:
    #         qry = "select Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(crMonth-4)  + " WHERE Student_Name=\"" + studentName + "\";"
    #         cursor.execute(qry)
    #         previousData4 = pd.DataFrame(cursor.fetchall(), columns=["Student Names", "Department", "Year", "Boarding Point", "Fee", "Paid", "Pending"])
    

    # privious_Data = [previousData1, previousData2, previousData3, previousData4]

    if crMonth == 1:
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            jan = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear-1) + "_" + str(12) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            dec = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear-1) + "_" + str(11) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            nov = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear-1) + "_" + str(10) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            oct = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear-1) + "_" + str(9) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            sep = cursor.fetchall()[0][0]
        except:
            pass

        # For Month 2
    elif crMonth == 2:
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            feb = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-1) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            jan = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear-1) + "_" + str(12) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            dec = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear-1) + "_" + str(11) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            nov = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear-1) + "_" + str(10) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            oct = cursor.fetchall()[0][0]
        except:
            pass

    # For Month 3
    elif crMonth == 3:
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            mar = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-1) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            feb = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-2) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            jan = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear-1) + "_" + str(12) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            dec = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear-1) + "_" + str(11) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            nov = cursor.fetchall()[0][0]
        except:
            pass

    # For Month 4
    elif crMonth == 4:
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            apr = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-1) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            mar = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-2) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            feb = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-3) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            jan = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear-1) + "_" + str(12) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            dec = cursor.fetchall()[0][0]
        except:
            pass

    # For Month 5
    elif crMonth == 5:
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            may = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-1) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            apr = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-2) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            mar = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-3) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            feb = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-4) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            jan = cursor.fetchall()[0][0]
        except:
            pass
    
    # For Month 6
    elif crMonth == 6:
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            jun = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-1) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            may = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-2) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            apr = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-3) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            mar = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-4) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            feb = cursor.fetchall()[0][0]
        except:
            pass
    
    # For Month 7
    elif crMonth == 7:
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            jul = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-1) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            jun = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-2) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            may = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-3) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            apr = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-4) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            mar = cursor.fetchall()[0][0]
        except:
            pass

    # For Month 8
    elif crMonth == 8:
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            aug = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-1) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            jul = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-2) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            jun = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-3) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            may = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-4) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            apr = cursor.fetchall()[0][0]
        except:
            pass
    
    # For Month 9
    elif crMonth == 9:
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            sep = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-1) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            aug = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-2) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            jul = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-3) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            jun = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-4) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            may = cursor.fetchall()[0][0]
        except:
            pass

    # For Month 10
    elif crMonth == 10:
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            oct = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-1) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            sep = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-2) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            aug = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-3) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            jul = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-4) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            jun = cursor.fetchall()[0][0]
        except:
            pass
    
    # For Month 11
    elif crMonth == 11:
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            nov = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-1) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            oct = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-2) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            sep = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-3) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            aug = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-4) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            jul = cursor.fetchall()[0][0]
        except:
            pass
    
    # For Month 12
    elif crMonth == 12:
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            dec = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-1) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            nov = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-2) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            oct = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-3) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            sep = cursor.fetchall()[0][0]
        except:
            pass
        try:
            qry = "SELECT Pending_Fee FROM bus_fee_details_" + str(crYear) + "_" + str(crMonth-4) + " WHERE Student_Name=\""+ studentName + "\""
            cursor.execute(qry)
            aug = cursor.fetchall()[0][0]
        except:
            pass

    # for mons in calcMonths:
    #     if mons == 9:
    #         qry = "SELECT Pending_Fee FROM bus_fee_details_2022_9 WHERE Student_Name=\""+ studentName + "\""
    #         cursor.execute(qry)
    #         data = cursor.fetchall()[0][0]
    #         sep = data
    #     if mons == 10:
    #         qry = "SELECT Pending_Fee FROM bus_fee_details_2022_10 WHERE Student_Name=\""+ studentName + "\""
    #         cursor.execute(qry)
    #         oct = cursor.fetchall()[0][0]

    return jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec, \
        jan + feb + mar + apr + may + jun + jul + aug + sep + oct + nov + dec