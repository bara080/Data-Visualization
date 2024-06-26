import plotly.offline as pyo
import pandas as pd
import plotly.graph_objects as go
from plotly import tools

#   multiple heat maps with subplots


df1 = pd.read_csv("./data/2010SantaBarbaraCA.csv")
df2 = pd.read_csv("./data/2010YumaAZ.csv")
df3 = pd.read_csv("./data/2010SitkaAK.csv")

trace1 = go.Heatmap(x = df1["DAY"], y= df1["LST_TIME"], z =df1["T_HR_AVG"], colorscale ="Jet" , zmin = 5, zmax = 40)

trace2 = go.Heatmap(x = df2["DAY"], y= df2["LST_TIME"], z =df2["T_HR_AVG"], colorscale ="Jet" , zmin = 5, zmax = 40)

trace3 = go.Heatmap(x = df3["DAY"], y= df3["LST_TIME"], z =df3["T_HR_AVG"], colorscale ="Jet" , zmin = 5, zmax = 40)

fig = tools.make_subplots(rows = 1, cols = 3, subplot_titles = ["SITKA AK", "SB CA", "YUMA AZ"], shared_yaxes = False)


fig.append_trace(trace1,1,1)

fig.append_trace(trace2,1,2)

fig.append_trace(trace1,1,3)

fig["layout"].update(title = "TEMPS FOR THREE CITIES", title_x = 0.5)

pyo.plot(fig)