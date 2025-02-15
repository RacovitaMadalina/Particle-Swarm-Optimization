import numpy as np


class Particle:
    def initialise_position(self):
        return np.random.uniform(self.lower_definition_limit, self.upper_definition_limit, size = self.dimension_no)

    def initialise_velocity(self):
        diff = abs(self.upper_definition_limit - self.lower_definition_limit)
        return np.random.uniform(-diff, diff, size = self.dimension_no)

    def update_velocity_in_respect_to_max_velocity_allowed(self):
        for i in range(len(self.velocity)):
            if self.velocity[i] > self.max_velocity_allowed:
                self.velocity[i] = self.max_velocity_allowed
            if self.velocity[i] < -self.max_velocity_allowed:
                self.velocity[i] = -self.max_velocity_allowed

    def update_position_in_respect_to_limits(self):
        for i in range(len(self.position)):
            if self.position[i] > self.upper_definition_limit:
                self.position[i] = self.upper_definition_limit
            if self.position[i] < self.lower_definition_limit:
                self.position[i] = self.lower_definition_limit

    def evaluate_position(self, position):
        return round(self.fitness_function(position), self.precision)

    def update_best_position_and_corresponding_eval(self, position):
        self.best_known_position = position
        self.eval_for_best_known_position = self.evaluate_position(self.best_known_position)

    def __init__(self, fitness, constants):
        self.fitness_function = fitness

        self.lower_definition_limit = constants.INTERVALS_OF_DEFINITION[fitness.__name__][0]
        self.upper_definition_limit = constants.INTERVALS_OF_DEFINITION[fitness.__name__][1]
        self.dimension_no = constants.DIMENSIONS_OF_THE_FUNCTION
        self.precision = constants.PRECISION
        self.max_velocity_allowed = constants.MAX_VELOCITY_ALLOWED

        self.position = self.initialise_position()
        self.velocity = self.initialise_velocity()
        self.evaluation = self.evaluate_position(self.position)

        # initialisation for the best particle's known position
        self.best_known_position = self.position
        self.eval_for_best_known_position = self.evaluate_position(self.best_known_position)
