from functions_to_be_minimized import *
from visualization import *

if __name__ == '__main__':

    # without visualisation
    # pso = PSO(de_jong)
    # pso.solve_pso_problem()

    # with visualisation
    visualiser = PSOVisualization(griewangk)
    visualiser.start_pso_visualizer()