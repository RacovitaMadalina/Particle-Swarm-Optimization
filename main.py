from functions_to_be_minimized import *
from visualization import *
from experiment_utils import Experiment

if __name__ == '__main__':

    # without visualisation
    # pso = PSO(de_jong)
    # pso.solve_pso_problem()

    # with visualisation
    # visualiser = PSOVisualization(griewangk)
    # visualiser.start_pso_visualizer()

    # 15 experiments on a fixed population + statistics
    experiment = Experiment(rastrigin)
    max_value, min_value, mean_value = experiment.run_experiment()
    print('Min = ', min_value, " Max = ", max_value, " Mean = ", mean_value)
