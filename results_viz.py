import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

from constants import results_file
from results import Results

def best_value_depending_on_generation(df, title, xgap, filename = None):
	for experiment_no in df["Experiment_no"].unique():
		y = df[df["Experiment_no"] == experiment_no]["Mean"]
		x = range(0, xgap * len(y), xgap)
		plt.plot(x, y)

	print(len(df["Experiment_no"].unique()))
	plt.title(title)
	#plt.show()

	if filename != None:
		plt.savefig(filename)

rastrigin_res = Results()
rastrigin_res.load("results/ratrigin.pickle")

rosenbrock_res = Results()
rosenbrock_res.load("results/rosenbrock.pickle")

sixhump_res = Results()
sixhump_res.load("results/sixhump.pickle")

griewangk_res = Results()
griewangk_res.load("results/griewangk.pickle")

pd.set_option("display.max_rows", len(rastrigin_res.df))
#print(rastrigin_res.df)
#exit(0)

# results.df.sort_values("Mean", inplace = True)
best_value_depending_on_generation(sixhump_res.df[(sixhump_res.df["Pop_size"] == 15) & (sixhump_res.df["Cognitive"] == 0.5)],
	"Evolution of best values for Six Hump function", 1, "images/sh cognitive 0.5, pop_size 15.png")
best_value_depending_on_generation(sixhump_res.df[(sixhump_res.df["Pop_size"] == 50) & (sixhump_res.df["Cognitive"] == 0.5)],
	"Evolution of best values for Six Hump function", 1, "images/sh cognitive 0.5, pop_size 50.png")
best_value_depending_on_generation(sixhump_res.df[(sixhump_res.df["Pop_size"] == 100) & (sixhump_res.df["Cognitive"] == 0.5)],
	"Evolution of best values for Six Hump function", 1, "images/sh cognitive 0.5, pop_size 100.png")
best_value_depending_on_generation(sixhump_res.df[(sixhump_res.df["Pop_size"] == 15) & (sixhump_res.df["Cognitive"] == 1)],
	"Evolution of best values for Six Hump function", 1, "images/sh cognitive 1, pop_size 15.png")
best_value_depending_on_generation(sixhump_res.df[(sixhump_res.df["Pop_size"] == 50) & (sixhump_res.df["Cognitive"] == 1)],
	"Evolution of best values for Six Hump function", 1, "images/sh cognitive 1, pop_size 50.png")
best_value_depending_on_generation(sixhump_res.df[(sixhump_res.df["Pop_size"] == 100) & (sixhump_res.df["Cognitive"] == 1)],
	"Evolution of best values for Six Hump function", 1, "images/sh cognitive 1, pop_size 100.png")

best_value_depending_on_generation(rosenbrock_res.df[rosenbrock_res.df["Cognitive"] == 0.5],
	"Evolution of best values for Rosenbrock function", 10, "images/rose cognitive 0.5, pop_size 250.png")
best_value_depending_on_generation(rosenbrock_res.df[rosenbrock_res.df["Cognitive"] == 1],
	"Evolution of best values for Rosenbrock function", 10, "images/rose cognitive 1, pop_size 250.png")

best_value_depending_on_generation(griewangk_res.df[griewangk_res.df["Cognitive"] == 0.5],
	"Evolution of best values for Griewangk function", 10, "images/griew cognitive 0.5, pop_size 250.png")
best_value_depending_on_generation(griewangk_res.df[griewangk_res.df["Cognitive"] == 1],
	"Evolution of best values for Griewangk function", 10, "images/griew cognitive 1, pop_size 250.png")
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
