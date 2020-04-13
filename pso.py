import numpy as np

from particle import Particle
from swarm import Swarm


class PSO:
    def __init__(self, function_to_be_minimized, constants):
        self.constants = constants
        self.precision = constants.PRECISION
        self.inertia = constants.INERTIA_WEIGHT
        self.cognitive = constants.COGNITIVE_WEIGHT
        self.social = constants.SOCIAL_WEIGHT
        self.max_velocity_allowed = constants.MAX_VELOCITY_ALLOWED

        self.pop_size = constants.POP_SIZE
        self.generations_no = constants.GENERATIONS_NO
        self.dimensions_no = constants.DIMENSIONS_OF_THE_FUNCTION

        self.fitness = function_to_be_minimized
        self.a = constants.INTERVALS_OF_DEFINITION[self.fitness.__name__][0]
        self.b = constants.INTERVALS_OF_DEFINITION[self.fitness.__name__][1]

        self.population = []
        self.swarm = Swarm(self.fitness, self.precision)

    # References for the algorithm:
    # 1. https://en.wikipedia.org/wiki/Particle_swarm_optimization
    # 2. https://profs.info.uaic.ro/~pmihaela/MOC/PSO.html

    def pop_initialisation(self):
        # initialise the population of particles (including positions and corresponding velocities)
        for i in range(self.pop_size):
            current_particle = Particle(self.fitness, self.constants)
            current_particle.update_velocity_in_respect_to_max_velocity_allowed()
            self.population.append(current_particle)

            # update swarm's best position and global minimum for the function
            self.swarm.update_swarm_by_considered_particle(current_particle)

    def run_one_iteration_pso_algorithm(self):
        for i in range(self.pop_size):
            current_particle = self.population[i]

            # velocity update in respect with inertia ratio, individual performance and global swarm improvement
            random_cognitive = np.random.random()
            random_social = np.random.random()

            inertia_update_ratio = self.inertia * current_particle.velocity
            cognitive_update_ratio = self.cognitive * random_cognitive * (current_particle.best_known_position - current_particle.position)
            social_update_ratio = self.social * random_social * (self.swarm.best_known_position - current_particle.position)

            current_particle.velocity = inertia_update_ratio + cognitive_update_ratio + social_update_ratio
            current_particle.update_velocity_in_respect_to_max_velocity_allowed()

            current_particle.position = current_particle.position + current_particle.velocity
            current_particle.update_position_in_respect_to_limits()

            #for i in range(len(current_particle.position)):
            #    assert current_particle.lower_definition_limit <= current_particle.position[i]
            #    assert current_particle.position[i] <= current_particle.upper_definition_limit

            # update fitness for current particle
            current_particle.evaluation = current_particle.evaluate_position(current_particle.position)

            # update individual and collective improvements

            # update improvements of best position that each particle had during last computation
            if self.population[i].evaluation < self.population[i].eval_for_best_known_position:
                self.population[i].update_best_position_and_corresponding_eval(self.population[i].position)

            # update swarm's best position and global minimum for the function
            self.swarm.update_swarm_by_considered_particle(self.population[i])

    def solve_pso_problem(self):
        self.pop_initialisation()

        current_generation_index = 0
        while current_generation_index < self.generations_no:
            self.run_one_iteration_pso_algorithm()

            current_generation_index += 1
            print("Generation = " + str(current_generation_index) +
                  ' __________ Swarm minimum = ' + str(self.swarm.global_minimum_found) + '\n')
