import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

# Generate random numbers with a seed of 42
np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

# Create a scatter plot with additional styling options
data = [go.Scatter(x=random_x, y=random_y, mode="markers",
                   marker=dict(size=12, color="rgb(51,200,150)",  symbol="pentagon",line={"width": 3}),  # Set marker attributes
                   )]

# Define layout settings
layout = go.Layout(
    title="Random Scatter Plot",
    title_x=0.5,  # Set the title's x position to the center
    xaxis={"title": "random x"},
    yaxis=dict(title="random y"),
    hovermode="closest"
)

# Create a figure
fig = go.Figure(data=data, layout=layout)

# Plot the scatter plot
pyo.plot(fig, filename="scatter.html")
