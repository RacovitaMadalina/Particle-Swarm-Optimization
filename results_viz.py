import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

from constants import results_file
from results import Results

results = Results()
results.load(results_file)

pd.set_option("display.max_rows", len(results.df))

print(results.df[results.df["Function"] == "griewangk"])
exit(0)

fig = plt.figure(figsize=(15, 15))

fig = px.scatter_3d(results.df[results.df["Mean"] < 30],
                    x='Inertia',
                    y='Cognitive',
                    z='Social',
                    color='Mean',
                    opacity=0.9,
                    size='Mean',
                    title='The effect of different configurations for inertia / cognitive / social parameters over the PSO results.')
fig.show()
