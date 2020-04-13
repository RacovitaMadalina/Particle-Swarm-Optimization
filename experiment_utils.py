import numpy as np
from copy import deepcopy

from pso import *


class Experiment:
    def establish_starting_population(self):
        pso = PSO(self.fitness, self.constants)
        pso.pop_initialisation()
        return pso

    def __init__(self, function_to_be_minimized, constants):
        self.fitness = function_to_be_minimized
        self.constants = constants

    def run_pso(self, experiment_no):
        pso = self.establish_starting_population()

        for current_generation_index in range(1, pso.generations_no + 1):
            pso.run_one_iteration_pso_algorithm()
            #print("Dim " + str(pso.dimensions_no) + " Experiment = " + str(experiment_no) +
            #      ' __________ Generation = ' + str(current_generation_index) +
            #      ' __________ Swarm minimum = ' + str(pso.swarm.global_minimum_found) + '\n')

        if experiment_no > 0:
            print("\033[F\033[K", end = '')
        print("Experiment_no", experiment_no, "Swarm minimum", pso.swarm.global_minimum_found)

        return pso.swarm.global_minimum_found

    def run_experiment(self):
        # the PSO will be run on the same population of particles for 15 times so that the non deterministic nature
        # will be emphasized
        mins_found_during_experiment = []

        for experiment_no in range(30):
            current_min = self.run_pso(experiment_no)
            mins_found_during_experiment.append(current_min)

        print("\033[F\033[K", end = '')

        return max(mins_found_during_experiment), min(mins_found_during_experiment), \
               np.mean(mins_found_during_experiment)
