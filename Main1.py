import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    sizeOfTV=[]
    TimeSpentOnTV=[]
    with open(data_path) as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            sizeOfTV.append(float(row["Size of TV"]))
            TimeSpentOnTV.append(float(row["Average"]))
    return{"x":sizeOfTV,"y":TimeSpentOnTV}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between the Size of the TV and the Time spent watching it is => ",correlation[0,1])

def setup():
    data_path="data2.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)

setup()

        