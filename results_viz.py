import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import plotly.express as px
import plotly

from results import Results

matplotlib.style.use('ggplot')


def best_value_depending_on_generation(df, title, xgap, filename=None):
    fig = plt.figure(figsize=(18, 12))

    for experiment_no in df["Experiment_no"].unique():
        y = df[df["Experiment_no"] == experiment_no]["Mean"]
        x = range(0, xgap * len(y), xgap)
        plt.plot(x, y, lw=0.6)

    #print(len(df["Experiment_no"].unique()))

    plt.title(title)
    plt.ylabel('Minimum found')
    plt.xlabel('Number of generations')
    # plt.show()

    if filename is not None:
        plt.savefig(filename)

res = Results()
res.load("results/results.pickle")
"""
rastrigin_res = Results()
rastrigin_res.load("results/rastrigin.pickle")

rosenbrock_res = Results()
rosenbrock_res.load("results/rosenbrock.pickle")

sixhump_res = Results()
sixhump_res.load("results/sixhump.pickle")

griewangk_res = Results()
griewangk_res.load("results/griewangk.pickle")

pd.set_option("display.max_rows", len(rastrigin_res.df))
# print(rastrigin_res.df)
# exit(0)

# results.df.sort_values("Mean", inplace = True)
best_value_depending_on_generation(
    sixhump_res.df[(sixhump_res.df["Pop_size"] == 15) & (sixhump_res.df["Cognitive"] == 0.5)],
    "Evolution of best values for Six Hump function", 1, "images/sh cognitive 0.5, pop_size 15.png")
best_value_depending_on_generation(
    sixhump_res.df[(sixhump_res.df["Pop_size"] == 50) & (sixhump_res.df["Cognitive"] == 0.5)],
    "Evolution of best values for Six Hump function", 1, "images/sh cognitive 0.5, pop_size 50.png")
best_value_depending_on_generation(
    sixhump_res.df[(sixhump_res.df["Pop_size"] == 100) & (sixhump_res.df["Cognitive"] == 0.5)],
    "Evolution of best values for Six Hump function", 1, "images/sh cognitive 0.5, pop_size 100.png")
best_value_depending_on_generation(
    sixhump_res.df[(sixhump_res.df["Pop_size"] == 15) & (sixhump_res.df["Cognitive"] == 1)],
    "Evolution of best values for Six Hump function", 1, "images/sh cognitive 1, pop_size 15.png")
best_value_depending_on_generation(
    sixhump_res.df[(sixhump_res.df["Pop_size"] == 50) & (sixhump_res.df["Cognitive"] == 1)],
    "Evolution of best values for Six Hump function", 1, "images/sh cognitive 1, pop_size 50.png")
best_value_depending_on_generation(
    sixhump_res.df[(sixhump_res.df["Pop_size"] == 100) & (sixhump_res.df["Cognitive"] == 1)],
    "Evolution of best values for Six Hump function", 1, "images/sh cognitive 1, pop_size 100.png")

best_value_depending_on_generation(rosenbrock_res.df[rosenbrock_res.df["Cognitive"] == 0.5],
                                   "Evolution of best values for Rosenbrock function", 10,
                                   "images/rose cognitive 0.5, pop_size 250.png")
best_value_depending_on_generation(rosenbrock_res.df[rosenbrock_res.df["Cognitive"] == 1],
                                   "Evolution of best values for Rosenbrock function", 10,
                                   "images/rose cognitive 1, pop_size 250.png")

best_value_depending_on_generation(griewangk_res.df[griewangk_res.df["Cognitive"] == 0.5],
                                   "Evolution of best values for Griewangk function", 10,
                                   "images/griew cognitive 0.5, pop_size 250.png")
best_value_depending_on_generation(griewangk_res.df[griewangk_res.df["Cognitive"] == 1],
                                   "Evolution of best values for Griewangk function", 10,
                                   "images/griew cognitive 1, pop_size 250.png")

best_value_depending_on_generation(rastrigin_res.df[rastrigin_res.df["Cognitive"] == 0.5],
                                   "Evolution of best values for Rastrigin function", 10,
                                   "images/rastrigin cognitive 0.5, pop_size 250.png")
best_value_depending_on_generation(rastrigin_res.df[rastrigin_res.df["Cognitive"] == 1],
                                   "Evolution of best values for Rastrigin function", 10,
                                   "images/rastrigin cognitive 1, pop_size 250.png")

# exit(0)
"""
fig = plt.figure(figsize=(15, 15))
fig = px.scatter_3d(res.df[(res.df["Function"] == "rastrigin") & (res.df["Mean"] < 60)],
                    x='Inertia',
                    y='Cognitive',
                    z='Social',
                    color='Mean',
                    opacity=0.9,
                    size='Mean',
                    title='The effect of different configurations for inertia /'
                          ' cognitive / social parameters over the PSO results.')
plotly.offline.plot(fig, filename='./images/Rastrigin_diff_weights_mean_less_than_60.html', auto_open=False)
# fig.show()
