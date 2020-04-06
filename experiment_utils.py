import numpy as np

from pso import *


class Experiment:
    def establish_starting_population(self):
        pso = PSO(self.fitness)
        pso.pop_initialisation()
        return pso.population, pso.swarm

    def __init__(self, function_to_be_minimized):
        self.fitness = function_to_be_minimized
        self.fixed_population, self.initial_swarm = self.establish_starting_population()

    def run_pso_for_given_population(self, pso, experiment_no):
        pso.population = self.fixed_population
        pso.swarm = self.initial_swarm

        current_generation_index = 0
        while current_generation_index < pso.generations_no:
            pso.run_one_iteration_pso_algorithm()
            current_generation_index += 1
            print("Experiment = " + str(experiment_no) +
                  ' __________ Generation = ' + str(current_generation_index) +
                  ' __________ Swarm minimum = ' + str(pso.swarm.global_minimum_found) + '\n')

        return pso.swarm.global_minimum_found

    def run_experiment(self):
        # the PSO will be run on the same population of particles for 15 times so that the non deterministic nature
        # will be emphasized
        mins_found_during_experiment = []

        for experiment_no in range(15):
            pso = PSO(self.fitness)
            current_min = self.run_pso_for_given_population(pso, experiment_no)
            mins_found_during_experiment.append(current_min)

        return max(mins_found_during_experiment), min(mins_found_during_experiment), \
               np.mean(mins_found_during_experiment)
