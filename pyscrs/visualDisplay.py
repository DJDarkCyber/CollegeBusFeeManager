import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
from pyscrs.conf import *



def barGraphAccordingToDept():
    timenow = datetime.datetime.now()
    curYear = timenow.year
    curMonth = timenow.month
    con = mysql.connector.connect(host=DBHOST, user=DBUSERNAME, password=DBPASSWORD, database=DBNAME)
    cursor = con.cursor()
    cursor.execute("SELECT * FROM bus_fee_details_" + str(curYear) + "_" + str(curMonth))
    qryResult = cursor.fetchall()

    dt = pd.DataFrame(qryResult, columns=["Student Name", "Department", "Year", "Boarding Point", "Total Fee", "Paid Fee", "Pending Fee"])
    
    depts = dt["Department"].value_counts().keys()
    depts = depts.to_list()
    np.random.shuffle(depts)

    totalPaidInfo = []
    for i in range(0, len(depts)):
        totalPaidInfo.append(len(dt["Department"][dt["Department"] == depts[i]][dt["Pending Fee"] != 0]))
    
    fig, ax = plt.subplots()
    ax.bar(x=depts, height=totalPaidInfo, color=[(x, 0.5, 0.7) for x in np.linspace(0.1, 1, num=len(depts))])
    
    def valuelabel(fee):
        for i in range(len(fee)):
            plt.text(i, fee[i], fee[i], ha="center", bbox=dict(facecolor="azure", alpha=0.7))
    
    valuelabel(totalPaidInfo)
    ax.set(title="Not Paid Students Count According To Department", xlabel="Departments", ylabel="Student Counts")
    fig.savefig("static/graphs/npAccToDept.png", transparent=True)


    # For Previous Month

    try:
        if curMonth == 1:
            cursor.execute("SELECT * FROM bus_fee_details_" + str(curYear-1) + "_" + str(12))
            qryResult = cursor.fetchall()

            dt = pd.DataFrame(qryResult, columns=["Student Name", "Department", "Year", "Boarding Point", "Total Fee", "Paid Fee", "Pending Fee"])
            
            depts = dt["Department"].value_counts().keys()
            depts = depts.to_list()
            np.random.shuffle(depts)

            totalPaidInfo = []
            for i in range(0, len(depts)):
                totalPaidInfo.append(len(dt["Department"][dt["Department"] == depts[i]][dt["Pending Fee"] != 0]))
            
            fig, ax = plt.subplots()
            ax.bar(x=depts, height=totalPaidInfo, color=[(x, 0.5, 0.7) for x in np.linspace(0.1, 1, num=len(depts))])
            
            def valuelabel(fee):
                for i in range(len(fee)):
                    plt.text(i, fee[i], fee[i], ha="center", bbox=dict(facecolor="azure", alpha=0.7))
            
            valuelabel(totalPaidInfo)
            ax.set(title="Not Paid Students Count According To Department", xlabel="Departments", ylabel="Student Counts")
            fig.savefig("static/graphs/npAccToDeptPrevious.png", transparent=True)
        else:
            cursor.execute("SELECT * FROM bus_fee_details_" + str(curYear) + "_" + str(curMonth-1))
            qryResult = cursor.fetchall()

            dt = pd.DataFrame(qryResult, columns=["Student Name", "Department", "Year", "Boarding Point", "Total Fee", "Paid Fee", "Pending Fee"])
            
            depts = dt["Department"].value_counts().keys()
            depts = depts.to_list()
            np.random.shuffle(depts)

            totalPaidInfo = []
            for i in range(0, len(depts)):
                totalPaidInfo.append(len(dt["Department"][dt["Department"] == depts[i]][dt["Pending Fee"] != 0]))
            
            fig, ax = plt.subplots()
            ax.bar(x=depts, height=totalPaidInfo, color=[(x, 0.5, 0.7) for x in np.linspace(0.1, 1, num=len(depts))])
            
            def valuelabel(fee):
                for i in range(len(fee)):
                    plt.text(i, fee[i], fee[i], ha="center", bbox=dict(facecolor="azure", alpha=0.7))
            
            valuelabel(totalPaidInfo)
            ax.set(title="Not Paid Students Count According To Department", xlabel="Departments", ylabel="Student Counts")
            fig.savefig("static/graphs/npAccToDeptPrevious.png", transparent=True)

    except:
        fig, ax = plt.subplots()
        ax.bar(x=[0], height=[0])
        ax.set_title("No Data Found!")
        fig.savefig("static/graphs/npAccToDeptPrevious.png", transparent=True)

    # Data of 2 Months ago

    try:
        if curMonth == 1:
            cursor.execute("SELECT * FROM bus_fee_details_" + str(curYear-1) + "_" + str(11))
            qryResult = cursor.fetchall()

            dt = pd.DataFrame(qryResult, columns=["Student Name", "Department", "Year", "Boarding Point", "Total Fee", "Paid Fee", "Pending Fee"])
            
            depts = dt["Department"].value_counts().keys()
            depts = depts.to_list()
            np.random.shuffle(depts)

            totalPaidInfo = []
            for i in range(0, len(depts)):
                totalPaidInfo.append(len(dt["Department"][dt["Department"] == depts[i]][dt["Pending Fee"] != 0]))
            
            fig, ax = plt.subplots()
            ax.bar(x=depts, height=totalPaidInfo, color=[(x, 0.5, 0.7) for x in np.linspace(0.1, 1, num=len(depts))])
            
            def valuelabel(fee):
                for i in range(len(fee)):
                    plt.text(i, fee[i], fee[i], ha="center", bbox=dict(facecolor="azure", alpha=0.7))
            
            valuelabel(totalPaidInfo)
            ax.set(title="Not Paid Students Count According To Department", xlabel="Departments", ylabel="Student Counts")
            fig.savefig("static/graphs/npAccToDeptPreviour.png", transparent=True)

        elif curMonth == 2:
            cursor.execute("SELECT * FROM bus_fee_details_" + str(curYear-1) + "_" + str(12))
            qryResult = cursor.fetchall()

            dt = pd.DataFrame(qryResult, columns=["Student Name", "Department", "Year", "Boarding Point", "Total Fee", "Paid Fee", "Pending Fee"])
            
            depts = dt["Department"].value_counts().keys()
            depts = depts.to_list()
            np.random.shuffle(depts)

            totalPaidInfo = []
            for i in range(0, len(depts)):
                totalPaidInfo.append(len(dt["Department"][dt["Department"] == depts[i]][dt["Pending Fee"] != 0]))
            
            fig, ax = plt.subplots()
            ax.bar(x=depts, height=totalPaidInfo, color=[(x, 0.5, 0.7) for x in np.linspace(0.1, 1, num=len(depts))])
            
            def valuelabel(fee):
                for i in range(len(fee)):
                    plt.text(i, fee[i], fee[i], ha="center", bbox=dict(facecolor="azure", alpha=0.7))
            
            valuelabel(totalPaidInfo)
            ax.set(title="Not Paid Students Count According To Department", xlabel="Departments", ylabel="Student Counts")
            fig.savefig("static/graphs/npAccToDeptPreviour.png", transparent=True)
        
        else:
            cursor.execute("SELECT * FROM bus_fee_details_" + str(curYear) + "_" + str(curMonth-2))
            qryResult = cursor.fetchall()

            dt = pd.DataFrame(qryResult, columns=["Student Name", "Department", "Year", "Boarding Point", "Total Fee", "Paid Fee", "Pending Fee"])
            
            depts = dt["Department"].value_counts().keys()
            depts = depts.to_list()
            np.random.shuffle(depts)

            totalPaidInfo = []
            for i in range(0, len(depts)):
                totalPaidInfo.append(len(dt["Department"][dt["Department"] == depts[i]][dt["Pending Fee"] != 0]))
            
            fig, ax = plt.subplots()
            ax.bar(x=depts, height=totalPaidInfo, color=[(x, 0.5, 0.7) for x in np.linspace(0.1, 1, num=len(depts))])
            
            def valuelabel(fee):
                for i in range(len(fee)):
                    plt.text(i, fee[i], fee[i], ha="center", bbox=dict(facecolor="azure", alpha=0.7))
            
            valuelabel(totalPaidInfo)
            ax.set(title="Not Paid Students Count According To Department", xlabel="Departments", ylabel="Student Counts")
            fig.savefig("static/graphs/npAccToDeptPreviour.png", transparent=True)

    except:
        fig, ax = plt.subplots()
        ax.bar(x=[0], height=[0])
        ax.set_title("No Data Found!")
        fig.savefig("static/graphs/npAccToDeptPreviour.png", transparent=True)



def pieGraphPercentageOfStudents():
    timenow = datetime.datetime.now()
    curYear = timenow.year
    curMonth = timenow.month
    con = mysql.connector.connect(host=DBHOST, user=DBUSERNAME, password=DBPASSWORD, database=DBNAME)
    cursor = con.cursor()
    cursor.execute("SELECT * FROM bus_fee_details_" + str(curYear) + "_" + str(curMonth))
    qryResult = cursor.fetchall()

    dt = pd.DataFrame(qryResult, columns=["Student Name", "Department", "Year", "Boarding Point", "Total Fee", "Paid Fee", "Pending Fee"])
    depts = dt["Department"].value_counts()
    

    # Generate Random Explodes

    exps = [0, 0.1, 0]
    explds = []
    for i in range(0, len(depts)):
        explds.append(exps[np.random.randint(0, 3)])
    

    fig, ax = plt.subplots()
    ax.pie(depts.values, labels=depts.keys(), autopct='%1.1f%%', explode=explds, shadow=True, colors=[(x, 0.5, 0.6) for x in np.linspace(0.1, 1, num=len(depts))])
    ax.set_title("Total No.Of Students in College")

    fig.savefig("static/graphs/percentageOfStudentsPie.png", transparent=True)


    # Get Data Of Previous Month

    depts = {"": 0}
    try:
        if curMonth == 1:
            cursor.execute("SELECT * FROM bus_fee_details_" + str(curYear-1) + "_" + str(12))
            qryResult = cursor.fetchall()
            dt = pd.DataFrame(qryResult, columns=["Student Name", "Department", "Year", "Boarding Point", "Total Fee", "Paid Fee", "Pending Fee"])
            depts = dt["Department"].value_counts()
            exps = [0, 0.1, 0]
            explds = []
            for i in range(0, len(depts)):
                explds.append(exps[np.random.randint(0, 3)])
            

            fig, ax = plt.subplots()
            ax.pie(depts.values, labels=depts.keys(), autopct='%1.1f%%', explode=explds, shadow=True, colors=[(x, 0.5, 0.6) for x in np.linspace(0.1, 1, num=len(depts))])
            ax.set_title("Total No.Of Students in College")

            fig.savefig("static/graphs/percentageOfStudentsPiePrevious.png", transparent=True)
        else:
            cursor.execute("SELECT * FROM bus_fee_details_" + str(curYear) + "_" + str(curMonth-1))
            qryResult = cursor.fetchall()
            dt = pd.DataFrame(qryResult, columns=["Student Name", "Department", "Year", "Boarding Point", "Total Fee", "Paid Fee", "Pending Fee"])
            depts = dt["Department"].value_counts()
            exps = [0, 0.1, 0]
            explds = []
            for i in range(0, len(depts)):
                explds.append(exps[np.random.randint(0, 3)])
            

            fig, ax = plt.subplots()
            ax.pie(depts.values, labels=depts.keys(), autopct='%1.1f%%', explode=explds, shadow=True, colors=[(x, 0.5, 0.6) for x in np.linspace(0.1, 1, num=len(depts))])
            ax.set_title("Total No.Of Students in College")

            fig.savefig("static/graphs/percentageOfStudentsPiePrevious.png", transparent=True)
    except:
        fig, ax = plt.subplots()
        ax.pie([0], [0])
        ax.set_title("No Data Found!")
        fig.savefig("static/graphs/percentageOfStudentsPiePrevious.png", transparent=True)


    # Data from 2 months ago
    
    try:
        if curMonth == 1:
            cursor.execute("SELECT * FROM bus_fee_details_" + str(curYear-1) + "_" + str(11))
            qryResult = cursor.fetchall()
            dt = pd.DataFrame(qryResult, columns=["Student Name", "Department", "Year", "Boarding Point", "Total Fee", "Paid Fee", "Pending Fee"])
            depts = dt["Department"].value_counts()
            exps = [0, 0.1, 0]
            explds = []
            for i in range(0, len(depts)):
                explds.append(exps[np.random.randint(0, 3)])
            

            fig, ax = plt.subplots()
            ax.pie(depts.values, labels=depts.keys(), autopct='%1.1f%%', explode=explds, shadow=True, colors=[(x, 0.5, 0.6) for x in np.linspace(0.1, 1, num=len(depts))])
            ax.set_title("Total No.Of Students in College")

            fig.savefig("static/graphs/percentageOfStudentsPiePreviour.png", transparent=True)

        elif curMonth == 2:
            cursor.execute("SELECT * FROM bus_fee_details_" + str(curYear-1) + "_" + str(12))
            qryResult = cursor.fetchall()
            dt = pd.DataFrame(qryResult, columns=["Student Name", "Department", "Year", "Boarding Point", "Total Fee", "Paid Fee", "Pending Fee"])
            depts = dt["Department"].value_counts()
            exps = [0, 0.1, 0]
            explds = []
            for i in range(0, len(depts)):
                explds.append(exps[np.random.randint(0, 3)])
            

            fig, ax = plt.subplots()
            ax.pie(depts.values, labels=depts.keys(), autopct='%1.1f%%', explode=explds, shadow=True, colors=[(x, 0.5, 0.6) for x in np.linspace(0.1, 1, num=len(depts))])
            ax.set_title("Total No.Of Students in College")

            fig.savefig("static/graphs/percentageOfStudentsPiePreviour.png", transparent=True)
        
        else:
            cursor.execute("SELECT * FROM bus_fee_details_" + str(curYear) + "_" + str(curMonth-2))
            qryResult = cursor.fetchall()
            dt = pd.DataFrame(qryResult, columns=["Student Name", "Department", "Year", "Boarding Point", "Total Fee", "Paid Fee", "Pending Fee"])
            depts = dt["Department"].value_counts()
            exps = [0, 0.1, 0]
            explds = []
            for i in range(0, len(depts)):
                explds.append(exps[np.random.randint(0, 3)])
            

            fig, ax = plt.subplots()
            ax.pie(depts.values, labels=depts.keys(), autopct='%1.1f%%', explode=explds, shadow=True, colors=[(x, 0.5, 0.6) for x in np.linspace(0.1, 1, num=len(depts))])
            ax.set_title("Total No.Of Students in College")

            fig.savefig("static/graphs/percentageOfStudentsPiePreviour.png", transparent=True)
    except:
        fig, ax = plt.subplots()
        ax.pie([0], [0])
        ax.set_title("No Data Found!")
        fig.savefig("static/graphs/percentageOfStudentsPiePreviour.png", transparent=True)


