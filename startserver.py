# Developer : Mr437
# Github Profile : https://github.com/DJDarkCyber
# Project Version : 0.1



## A Bus Fee Management using Web Application



from flask import Flask, url_for, render_template, request, redirect, flash
from pyscrs import searchstud
from pyscrs import payAmountFunc
from pyscrs import addDelEd, initializer, endSemester, visualDisplay, sortout, overviewer


app = Flask("__name__")

app.secret_key="437437437437437437437"




@app.route("/")
def main():
    initializer.initialize()
    print("Initialized")
    return render_template("index.html")

@app.route("/payfees", methods=["POST", "GET"])
def feesManager():
    if request.method == "POST":
        studentName = request.form["STUDNAME"]
        foundStus, foundDepts, foundYear, boardingPoint, foundTtlFee, foundPendFee,  = searchstud.searchit(studentName)
        if len(foundStus) < 1:
            flash("No Students where found with this name")
            print("No Students found")
        return render_template("payfee.html", stud=foundStus, dept=foundDepts, year=foundYear, total=foundTtlFee, pend=foundPendFee, len=len(foundStus), meth="POST", board=boardingPoint)
    else:
        return render_template("payfee.html", stud="")

@app.route("/payAmount", methods=["POST", "GET"])
def payAmount():
    if request.method == "POST":
        studentName = request.form["STUDENTNAME"]
        studentDepartment = request.form["DEPARTMENT"]
        studentYear = request.form["YEAR"]
        studentTotal = request.form["TOTAL"]
        studentPending = request.form["PEND"]
        studentBoarding = request.form["BOARD"]
        jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec, total = searchstud.displayInMonths(studentName=studentName)
        return render_template("payAmount.html", Stud=studentName, Dept=studentDepartment, Year=studentYear, Total=studentTotal, Pend=studentPending, Board=studentBoarding,
         Jan=jan, Feb=feb, Mar=mar, Apr=apr, May=may, Jun=jun, Jul=jul, Aug=aug, Sep=sep, Oct=oct, Nov=nov, Dec=dec, TotalFee=total
        )
    return "None"

@app.route("/amountPayed", methods=["POST", "GET"])
def amountPayed():
    if request.method == "POST":
        studentName = request.form["STUDENTNAME"]
        studentDepartment = request.form["DEPARTMENT"]
        studentYear = request.form["YEAR"]
        studentBatch = request.form["BATCH"]
        studentTotal = request.form["TOTAL"]
        studentBoarding = request.form["BOARD"]


        try:
            studentJanFee = request.form["JAN"]
        except KeyError:
            studentJanFee = 0
        try:
            studentFebFee = request.form["FEB"]
        except KeyError:
            studentFebFee = 0
        try:
            studentMarFee = request.form["MAR"]
        except KeyError:
            studentMarFee = 0
        try:
            studentAprFee = request.form["APR"]
        except KeyError:
            studentAprFee = 0
        try:
            studentMayFee = request.form["MAY"]
        except KeyError:
            studentMayFee = 0
        try:
            studentJunFee = request.form["JUN"]
        except KeyError:
            studentJunFee = 0
        try:
            studentJulFee = request.form["JUL"]
        except KeyError:
            studentJulFee = 0
        try:
            studentAugFee = request.form["AUG"]
        except KeyError:
            studentAugFee = 0
        try:
            studentSepFee = request.form["SEP"]
        except KeyError:
            studentSepFee = 0
        try:
            studentOctFee = request.form["OCT"]
        except KeyError:
            studentOctFee = 0
        try:
            studentNovFee = request.form["NOV"]
        except KeyError:
            studentNovFee = 0
        try:
            studentDecFee = request.form["DEC"]
        except KeyError:
            studentDecFee = 0


        payAmountFunc.payAmount(studentName, payMonths=[studentJanFee, studentFebFee, studentMarFee, studentAprFee, studentMayFee, studentJunFee, studentJulFee, studentAugFee, studentSepFee, studentOctFee, studentNovFee, studentDecFee])
        jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec, total = searchstud.displayInMonths(studentName=studentName)
        return render_template("amountpayed.html", stud=studentName, dept=studentDepartment, year=studentYear, batch=studentBatch, total=studentTotal, board=studentBoarding, Jan=jan, Feb=feb, Mar=mar, Apr=apr, May=may, Jun=jun, Jul=jul, Aug=aug, Sep=sep, Oct=oct, Nov=nov, Dec=dec, TotalFee=total)
    return "Amount Payed!"

@app.route("/AddOrDelete", methods=["POST", "GET"])
def addOrDeleteSelect():
    return render_template("addAndDel.html")

@app.route("/addData", methods=["POST", "GET"])
def addData():
    if request.method == "GET":
        return render_template("addData.html")
    elif request.method == "POST":
        studentName = request.form["STUDNAME"]
        studentDept = request.form["DEPART"]
        studentYear = request.form["YEAR"]
        studentBoard = request.form["BOARDPOINT"]
        studentFee = request.form["FEE"]
        studentPaid = request.form["PAIDFEE"]
        studentPend = request.form["PENDINGFEE"]
        addDelEd.addData(studentName, studentDept, studentYear, studentBoard, studentFee, studentPaid, studentPend)
        return render_template("addData.html", meth="post")

@app.route("/deleteData", methods=["POST", "GET"])
def deleteData():
    delConf = None
    try:
        delConf = request.form["delConf"]
    except Exception:
        pass
    if request.method == "GET":
        return render_template("searchToDel.html")


    elif request.method == "POST" and delConf == "DeleteConf":
        addDelEd.deleteData(request.form["STUDENTNAME"], request.form["DEPARTMENT"], request.form["YEAR"], request.form["BOARD"], request.form["TOTAL"], None, None)
        return render_template("searchToDel.html", isDeleted="Deleted")

    elif request.method == "POST":
        studentName = request.form["STUDNAME"]
        foundStus, foundDepts, foundYear, boardingPoint, foundTtlFee, foundPendFee,  = searchstud.searchit(studentName)
        if len(foundStus) < 1:
            flash("No Students where found with this name")
            print("No Students found")
        return render_template("searchToDel.html", stud=foundStus, dept=foundDepts, year=foundYear, total=foundTtlFee, pend=foundPendFee, len=len(foundStus), meth="POST", board=boardingPoint)


@app.route("/editData", methods=["POST", "GET"])
def editData():

    edConf = None
    try:
        edConf = request.form["edConf"]
    except Exception:
        pass

    if request.method == "GET":
        return render_template("editData.html")

    elif request.method == "POST" and edConf == "EditConf":
        addDelEd.editData(request.form["STUDENTNAME"], request.form["DEPARTMENT"], request.form["YEAR"], request.form["BOARD"], request.form["TOTAL"], request.form["PEND"], oldstud=request.form["OLDSTUDENTNAME"], olddept=request.form["OLDDEPARTMENT"], oldyear=request.form["OLDYEAR"])
        return render_template("editData.html", isEdited="Edited")
    elif request.method == "POST":
        studentName = request.form["STUDNAME"]
        foundStus, foundDepts, foundYear, boardingPoint, foundTtlFee, foundPendFee,  = searchstud.searchit(studentName)
        if len(foundStus) < 1:
            flash("No Students where found with this name")
            print("No Students found")
        return render_template("editData.html", stud=foundStus, dept=foundDepts, year=foundYear, total=foundTtlFee, pend=foundPendFee, len=len(foundStus), meth="POST", board=boardingPoint)


@app.route("/EndYear", methods=["POST", "GET"])
def endTheYear():
    if request.method == "POST":
        endSemester.EndTheSem()
        return render_template("endTheYear.html", meth="post")
    else:
        return render_template("endTheYear.html", meth="get")


@app.route("/VisualView")
def visualView():
    visualDisplay.barGraphAccordingToDept()
    visualDisplay.pieGraphPercentageOfStudents()
    return render_template("visualView.html")



@app.route("/SortOut", methods=["POST", "GET"])
def sortOutDetails():
    currentMonData, previousData, prevousData2, prevousData3, prevousData4 = sortout.getNotPaidInfo()
    print("I am executing")
    if request.method == "GET":
        lenOfData1 = len(currentMonData)
        lenOfData2 = len(previousData)
        lenOfData3 = len(prevousData2)
        lenOfData4 = len(prevousData3)
        lenOfData5 = len(prevousData4)
        return render_template("sortoutdts.html", ln1=lenOfData1, ln2=lenOfData2, ln3=lenOfData3, ln4=lenOfData4, ln5=lenOfData5, curMon=currentMonData, prev1=previousData, prev2=prevousData2, prev3=prevousData3, prev4=prevousData4, meth="get")
    elif request.method == "POST":
        lenOfData1 = len(currentMonData)
        lenOfData2 = len(previousData)
        lenOfData3 = len(prevousData2)
        lenOfData4 = len(prevousData3)
        lenOfData5 = len(prevousData4)

        sortout.exportOverviewData(currentMonData, previousData, prevousData2, prevousData3, prevousData4)

        return render_template("sortoutdts.html", ln1=lenOfData1, ln2=lenOfData2, ln3=lenOfData3, ln4=lenOfData4, ln5=lenOfData5, curMon=currentMonData, prev1=previousData, prev2=prevousData2, prev3=prevousData3, prev4=prevousData4, meth="post")


@app.route("/overview")
def overviewData():
    totalNoOfStuds = overviewer.getTotalNoOfStudents()
    totalNoOfNotPaid = overviewer.getTotalNumberOfNotPaid()
    totalNoOfDepts = overviewer.getTotalNoOfDepts()
    totalStudsInDepts = overviewer.getTotalNoOfStudentsInDepts().items()
    # totalNamesOfDepts = totalStudsInDepts.keys()
    totalBrdingPoints = overviewer.getAllBoardingPoaints().items()


    
    return render_template("overview.html", totalStds=totalNoOfStuds, totalNotPaid=totalNoOfNotPaid, depts=totalNoOfDepts, totalStudsInDept=totalStudsInDepts, totalBoarding=totalBrdingPoints)


if __name__ == "__main__":
    app.run(debug=True)

