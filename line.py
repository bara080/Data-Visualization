import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

# Generate random numbers with a seed of 42
np.random.seed(56)
x_values = np.linspace(0, 1, 100)
y_values = np.random.randn(100)

# Create a scatter plot with additional styling options
trace = go.Scatter(x=x_values, y=y_values + 5, mode="markers", name="markers")

trace1 = go.Scatter(x=x_values, y=y_values, mode="lines", name="my_lines")

trace2 = go.Scatter(x=x_values, y=y_values - 5, mode="lines+markers", name="my_favorite")

data = [trace, trace1, trace2]

# Define layout settings
layout = go.Layout(
    title="Line charts",
    title_x=0.5,  # Set the title's x position to the center
    
)

# Create a figure
fig = go.Figure(data=data, layout=layout)

# Plot the scatter plot
pyo.plot(fig, filename="Linechart.html")
