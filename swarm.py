class Swarm:
    def update_best_position_and_corresponding_eval(self, position):
        self.best_known_position = position
        self.global_minimum_found = round(self.fitness(self.best_known_position), self.precision)

    def update_swarm_by_considered_particle(self, particle):
        if self.best_known_position is None:
            self.update_best_position_and_corresponding_eval(particle.position)
        else:
            eval_best_known_position_for_current_particle = round(
                self.fitness(particle.best_known_position),
                self.precision)

            if eval_best_known_position_for_current_particle < self.global_minimum_found:
                self.update_best_position_and_corresponding_eval(particle.best_known_position)

    def __init__(self, fitness_function, precision):
        self.fitness = fitness_function
        self.precision = precision
        self.best_known_position = None
        self.global_minimum_found = None