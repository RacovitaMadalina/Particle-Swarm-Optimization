from pso import *
from functions_to_be_minimized import *

if __name__ == '__main__':
    pso = PSO(rastrigin)
    pso.solve_pso_problem()