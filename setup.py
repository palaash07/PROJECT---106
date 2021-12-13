import plotly.express as px
import csv 
import numpy as np

def plotgraph(datapath):
    with open(datapath,newline = "") as f:
        reader = csv.DictReader(f)
        fig = px.scatter(reader,x = "Coffee in ml",y = "sleep in hours")
        fig.show()

def getdatasource(datapath):
    Coffeeinml = []
    sleepinhours = []
    with open(datapath,newline = "") as f:
        reader = csv.DictReader(f)
        for i in reader:
            Coffeeinml.append(float(i["Coffee in ml"]))
            sleepinhours.append(float(i["sleep in hours"]))
    return {"x":Coffeeinml,"y":sleepinhours}

def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])  
    print(correlation[0,1])

def setup():
    datapath = "sleepcoffe.csv"
    plotgraph(datapath)
    r = getdatasource(datapath)
    findcorrelation(r)

setup()



