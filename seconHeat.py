#   import all necessary libraries
import plotly.graph_objs as go
import pandas as pd
import plotly.offline as pyo


#  objectives : Using the flights datasets available
#   create a heatmap with the following

#  x-axis = "year"
#  y-axis = "month"
#  z-axis(color) = "passengers"
# 

df = pd.read_csv("./data/flights.csv")
print(df.columns)

#  Define a data variable

data = [
    go.Heatmap(
        x = df["year"],
        y = df["month"],
        z = df["passengers"]
    )]

#  define the layout
layout = go.Layout(title = "Title")

#  create a fig from data and layout and plot fig

fig = go.Figure(data=data, layout = layout)

pyo.plot(fig)