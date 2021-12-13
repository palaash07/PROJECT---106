import plotly.express as px
import csv 
import numpy as np

def plotgraph(datapath):
    with open(datapath,newline = "") as f:
        reader = csv.DictReader(f)
        fig = px.scatter(reader,x = "Days Present",y = "Marks In Percentage")
        fig.show()

def getdatasource(datapath):
    MarksInPercentage = []
    DaysPresent= []
    with open(datapath,newline = "") as f:
        reader = csv.DictReader(f)
        for i in reader:
            DaysPresent.append(int(i["Days Present"]))
            MarksInPercentage.append(float(i["Marks In Percentage"]))
    return {"x":DaysPresent,"y":MarksInPercentage}

def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])  
    print(correlation[0,1])

def setup():
    datapath = "student.csv"
    plotgraph(datapath)
    r = getdatasource(datapath)
    findcorrelation(r)

setup()



