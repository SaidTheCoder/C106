import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    MarksInPercentage=[]
    DaysPresent=[]
    with open(data_path) as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            MarksInPercentage.append(float(row["Marks In Percentage"]))
            DaysPresent.append(float(row["Days Present"]))
    return{"x":MarksInPercentage,"y":DaysPresent}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between the marks in percentage and the days present are => ",correlation[0,1])

def setup():
    data_path="data3.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)

setup()

        