import csv
import plotly.express as px

with open("data2.csv") as f:
    df=csv.DictReader(f)
    fig=px.scatter(df,x="Size of TV",y="Average")
    fig.show()