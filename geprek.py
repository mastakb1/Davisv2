pip install bokeh

from bokeh.plotting import figure, output_file, show
from bokeh.palettes import magma
import pandas as pd


# instantiating the figure object
graph = figure(title = "Bokeh Scatter Graph")

# reading the database
data = pd.read_csv("tips.csv")

color = magma(256)

# plotting the graph
graph.scatter(data['total_bill'], data['tip'], color=color)

# displaying the model
show(graph)
