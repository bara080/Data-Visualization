import plotly.offline as pyo
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("./data/2010SantaBarbaraCA.csv")

print(df.columns)

data = [go.Heatmap(
    x =df["DAY"],
    y= df["LST_TIME"],
    z= df["T_HR_AVG"].values.tolist()
)]

layout = go.Layout(title= "SB CA TEMPS")

fig =  go.Figure(data=data, layout=layout)

pyo.plot(fig)