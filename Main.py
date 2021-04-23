import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    icecream_sales=[]
    colddrink_sales=[]
    with open(data_path) as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            icecream_sales.append(float(row["Temperature"]))
            colddrink_sales.append(float(row["Ice-cream Sales"]))
    return{"x":icecream_sales,"y":colddrink_sales}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between the temperature and the icecream sales=> ",correlation[0,1])

def setup():
    data_path="Data1.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)

setup()

        