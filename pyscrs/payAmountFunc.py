import pandas as pd
import mysql.connector
import datetime
from pyscrs.conf import *

crTime = datetime.datetime.now()
crMonth = crTime.month
crYear = crTime.year

def payAmount(studentName, payMonths):
    # busdetails = pd.read_excel("data/studentFeeInfo/Bus-Fee-Data.xlsx", sheet_name=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    # for i in range(0, len(payMonths)):
    #     print(payMonths[i])
    #     print(int(busdetails[i]["Pending Fees"][ busdetails[i]["Student Name"] == studentName].item()))
    #     busdetails[i]["Pending Fees"][ busdetails[i]["Student Name"] == studentName] = int(busdetails[i]["Pending Fees"][ busdetails[i]["Student Name"] == studentName].item()) - int(payMonths[i])
    
    # with pd.ExcelWriter("data/studentFeeInfo/Bus-Fee-Data.xlsx") as writer:
    #     busdetails[0].to_excel(writer, sheet_name="January", index=False)
    #     busdetails[1].to_excel(writer, sheet_name="Feburary", index=False)
    #     busdetails[2].to_excel(writer, sheet_name="March", index=False)
    #     busdetails[3].to_excel(writer, sheet_name="April", index=False)
    #     busdetails[4].to_excel(writer, sheet_name="May", index=False)
    #     busdetails[5].to_excel(writer, sheet_name="June", index=False)
    #     busdetails[6].to_excel(writer, sheet_name="July", index=False)
    #     busdetails[7].to_excel(writer, sheet_name="August", index=False)
    #     busdetails[8].to_excel(writer, sheet_name="September", index=False)
    #     busdetails[9].to_excel(writer, sheet_name="October", index=False)
    #     busdetails[10].to_excel(writer, sheet_name="November", index=False)
    #     busdetails[11].to_excel(writer, sheet_name="December", index=False)
    con = mysql.connector.connect(host=DBHOST, user=DBUSERNAME, password=DBPASSWORD, database=DBNAME)
    cursor = con.cursor()
    # cursor.execute("SELECT ")
    janFee, febFee, marFee, aprFee, mayFee, junFee, julFee, augFee, sepFee, octFee, novFee, decFee = payMonths

    # From January

    if crMonth == 1:
        # For Current Month
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(janFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(janFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 1
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear-1) + "_" + str(12) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(decFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear-1) + "_" + str(12) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(decFee)
            qry = "UPDATE bus_fee_details_" + str(crYear-1) + "_" + str(12) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 2
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear-1) + "_" + str(11) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(novFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear-1) + "_" + str(11) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(novFee)
            qry = "UPDATE bus_fee_details_" + str(crYear-1) + "_" + str(11) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 3
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear-1) + "_" + str(10) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(octFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear-1) + "_" + str(10) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(octFee)
            qry = "UPDATE bus_fee_details_" + str(crYear-1) + "_" + str(10) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # Previous Month 4
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear-1) + "_" + str(9) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(sepFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear-1) + "_" + str(9) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(sepFee)
            qry = "UPDATE bus_fee_details_" + str(crYear-1) + "_" + str(9) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass
        
    # From Feburary
    elif crMonth == 2:
        # For Current Month
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(febFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(febFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 1
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(1) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(janFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(1) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(janFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(1) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 2
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear-1) + "_" + str(12) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(decFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear-1) + "_" + str(12) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(decFee)
            qry = "UPDATE bus_fee_details_" + str(crYear-1) + "_" + str(12) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 3
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear-1) + "_" + str(11) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(novFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear-1) + "_" + str(11) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(novFee)
            qry = "UPDATE bus_fee_details_" + str(crYear-1) + "_" + str(11) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # Previous Month 4
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear-1) + "_" + str(10) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(octFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear-1) + "_" + str(10) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(octFee)
            qry = "UPDATE bus_fee_details_" + str(crYear-1) + "_" + str(10) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # From March
    elif crMonth == 3:
        # For Current Month
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(marFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(marFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 1
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(2) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(febFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(2) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(febFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(2) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 2
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(1) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(janFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(1) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(janFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(1) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 3
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear-1) + "_" + str(12) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(decFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear-1) + "_" + str(12) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(decFee)
            qry = "UPDATE bus_fee_details_" + str(crYear-1) + "_" + str(12) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # Previous Month 4
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear-1) + "_" + str(11) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(novFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear-1) + "_" + str(11) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(novFee)
            qry = "UPDATE bus_fee_details_" + str(crYear-1) + "_" + str(11) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass


        # From April
    elif crMonth == 4:
        # For Current Month
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(aprFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(aprFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 1
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(3) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(marFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(3) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(marFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(3) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 2
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(2) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(febFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(2) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(febFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(2) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 3
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(1) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(janFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(1) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(janFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(1) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # Previous Month 4
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear-1) + "_" + str(12) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(decFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear-1) + "_" + str(12) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(decFee)
            qry = "UPDATE bus_fee_details_" + str(crYear-1) + "_" + str(12) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass
    

        # From May
    elif crMonth == 5:
        # For Current Month
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(mayFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(mayFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 1
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(4) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(aprFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(4) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(aprFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(4) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 2
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(3) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(marFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(3) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(marFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(3) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 3
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(2) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(febFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(2) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(febFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(2) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # Previous Month 4
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(1) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(janFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(1) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(janFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(1) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

    
    # For June
    elif crMonth == 6:
        # For Current Month
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(junFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(junFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 1
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(5) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(mayFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(5) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(mayFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(5) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 2
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(4) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(aprFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(4) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(aprFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(4) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 3
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(3) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(marFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(3) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(marFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(3) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # Previous Month 4
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(2) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(febFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(2) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(febFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(2) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

    # For July
    elif crMonth == 7:
        # For Current Month
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(julFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(julFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 1
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(6) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(junFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(6) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(junFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(6) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 2
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(5) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(mayFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(5) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(mayFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(5) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 3
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(4) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(aprFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(4) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(aprFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(4) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # Previous Month 4
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(3) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(marFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(3) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(marFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(3) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

    # For August
    elif crMonth == 8:
        # For Current Month
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(augFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(augFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 1
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(7) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(julFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(7) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(julFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(7) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 2
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(6) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(junFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(6) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(junFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(6) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 3
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(5) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(mayFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(5) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(mayFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(5) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # Previous Month 4
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(4) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(aprFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(4) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(aprFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(4) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

    # For September
    elif crMonth == 9:
        # For Current Month
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(sepFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(sepFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 1
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(8) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(augFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(8) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(augFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(8) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 2
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(7) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(julFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(7) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(julFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(7) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 3
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(6) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(junFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(6) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(junFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(6) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # Previous Month 4
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(5) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(mayFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(5) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(mayFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(5) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

    # For Octomber
    elif crMonth == 10:
        # For Current Month
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(octFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(octFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 1
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(9) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(sepFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(9) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(sepFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(9) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 2
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(8) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(augFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(8) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(augFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(8) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 3
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(7) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(julFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(7) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(julFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(7) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # Previous Month 4
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(6) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(junFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(6) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(junFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(6) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass
    
    # For November
    elif crMonth == 11:
        # For Current Month
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(novFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(novFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 1
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(10) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(octFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(10) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(octFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(10) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 2
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(9) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(sepFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(9) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(sepFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(9) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 3
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(8) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(augFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(8) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(augFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(8) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # Previous Month 4
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(7) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(julFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(7) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(julFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(7) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

    # For December
    elif crMonth == 12:
        # For Current Month
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(decFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(decFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(crMonth) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 1
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(11) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(novFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(11) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(novFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(11) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 2
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(10) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(octFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(10) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(octFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(10) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # For Previous Month 3
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(9) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(sepFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(9) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(sepFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(9) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

        # Previous Month 4
        try:
            qry = "SELECT Pending_Fee from bus_fee_details_" + str(crYear) + "_" + str(8) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            pendingData = cursor.fetchall()
            pendFee = int(pendingData[0][0]) - int(augFee)
            qry = "SELECT Paid_Fee from bus_fee_details_" + str(crYear) + "_" + str(8) + " WHERE Student_Name=\"" + studentName + "\""
            cursor.execute(qry)
            paidfeeData = cursor.fetchall()
            paidFee = int(paidfeeData[0][0]) + int(augFee)
            qry = "UPDATE bus_fee_details_" + str(crYear) + "_" + str(8) + " SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
            cursor.execute(qry)
        except:
            pass

    # for i in range(0, 12):
    #     if payMonths[i] != 0 and i==8:
    #         qry = "SELECT Pending_Fee from bus_fee_details_2022_9 WHERE Student_Name=\"" + studentName + "\""
    #         cursor.execute(qry)
    #         pendingData = cursor.fetchall()
    #         pendFee = int(pendingData[0][0]) - int(payMonths[i])
    #         qry = "SELECT Paid_Fee from bus_fee_details_2022_9 WHERE Student_Name=\"" + studentName + "\""
    #         cursor.execute(qry)
    #         paidfeeData = cursor.fetchall()
    #         paidFee = int(paidfeeData[0][0]) + int(payMonths[i])
    #         print("[+] Updated")
    #         qry = "UPDATE bus_fee_details_2022_9 SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
    #         cursor.execute(qry)
    #     if payMonths[i] != 0 and i==9:
    #         qry = "SELECT Pending_Fee from bus_fee_details_2022_10 WHERE Student_Name=\"" + studentName + "\""
    #         cursor.execute(qry)
    #         pendingData = cursor.fetchall()
    #         pendFee = int(pendingData[0][0]) - int(payMonths[i])
    #         qry = "SELECT Paid_Fee from bus_fee_details_2022_10 WHERE Student_Name=\"" + studentName + "\""
    #         cursor.execute(qry)
    #         paidfeeData = cursor.fetchall()
    #         paidFee = int(paidfeeData[0][0]) + int(payMonths[i])
    #         print("[+] Updated")
    #         qry = "UPDATE bus_fee_details_2022_10 SET Pending_Fee=\'"+ str(pendFee) + "\', Paid_Fee=\'" + str(paidFee) + "\' WHERE Student_Name=\'" + str(studentName) + "\'"
    #         cursor.execute(qry)
    
    con.commit()