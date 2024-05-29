#   IMPORT ALL NEEDED 
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd


#  Create a pandas DataFrame from 210YumaAz.csv
# get the data

df = pd.read_csv("2010YumaAZ.csv")

# list of days

days = ["TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY","SATURDAY", "SUNDAY", "MONDAY"]


data = []

for day in days:
    # Iterate
    trace = go.Scatter(x = df["LST_TIME"], y = df[df["DAY"] == day]["T_HR_AVG"],
                       mode ="lines" , name = day)
    data.append(trace)

# use a for loop ( or list comprehension to create a trace for the data list)


#  Define the layout

layout = go.Layout(title= "Daily Temperature Average")
#  create a fig and from the data and layout and plot

fig = go.Figure(data =data, layout = layout)

pyo.plot(fig)