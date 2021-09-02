import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Marks-In-Percentage", y="Days-Present")
        fig.show()

def getDataSource(data_path):
    marks = []
    days_present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Marks-In-Percentage"]))
            days_present.append(float(row["Days-Present"]))

    return {"x" : marks, "y": days_present}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks vs Days-Present is :-  \n--->",correlation[0,1])

def setup():
    data_path  = "marksVSdays.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()