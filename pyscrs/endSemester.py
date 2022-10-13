import mysql.connector
import datetime
from pyscrs.conf import *



def EndTheSem():
    timeNow = datetime.datetime.now()
    crtMonth = timeNow.month
    crtYear = timeNow.year
    con = mysql.connector.connect(host=DBHOST, user=DBUSERNAME, password=DBPASSWORD, database=DBNAME)
    cursor = con.cursor()
    cursor.execute("DELETE FROM bus_fee_details_" + str(crtYear) + "_" + str(crtMonth) + " WHERE Year=4")
    cursor.execute("UPDATE bus_fee_details_" + str(crtYear) + "_" + str(crtMonth) + " SET Year=Year+1 WHERE Year=3")
    cursor.execute("UPDATE bus_fee_details_" + str(crtYear) + "_" + str(crtMonth) + " SET Year=Year+1 WHERE Year=2")
    cursor.execute("UPDATE bus_fee_details_" + str(crtYear) + "_" + str(crtMonth) + " SET Year=Year+1 WHERE Year=1")
    con.commit()