import matplotlib.pyplot as plt
import matplotlib.animation as animation

from pso import PSO
from mpl_toolkits.mplot3d import Axes3D


class PSOVisualization:
    def configure_axes(self):
        self.ax.set_xlabel('x[0]')
        self.ax.set_ylabel('x[1]')
        self.ax.set_zlabel('Particle\'s fitness')

        self.ax.set_xlim3d(self.pso.a, self.pso.b)
        self.ax.set_ylim3d(self.pso.a, self.pso.b)
        self.ax.set_zlim3d(min(self.z_values) - 1, max(self.z_values) + 1)

    def update_3d_visualization(self, generation_no):

        # collect information for 3d visualization
        for i in range(self.pso.pop_size):
            self.x_coords[i] = self.pso.population[i].position[0]
            self.y_coords[i] = self.pso.population[i].position[1]
            self.z_values[i] = self.pso.population[i].evaluation

        self.configure_axes()

        self.graph.set_data(self.x_coords, self.y_coords)
        self.graph.set_3d_properties(self.z_values)

        self.title.set_text('function = ' + self.fitness.__name__ +
                            '\nbest_found = ' + str(self.pso.swarm.global_minimum_found) +
                            '\ngeneration_no = ' + str(generation_no))

        self.pso.run_one_iteration_pso_algorithm()
        return self.title, self.graph,

    def __init__(self, fitness):
        self.pso = PSO(fitness)
        self.fitness = fitness

        self.fig = plt.figure(figsize=(15, 15))
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.title = self.ax.set_title('')

        # initialization of the particles coords for the 3d visualisation
        self.x_coords = [0 for _ in range(self.pso.pop_size)]
        self.y_coords = [0 for _ in range(self.pso.pop_size)]
        self.z_values = [0 for _ in range(self.pso.pop_size)]

        self.graph, = self.ax.plot(xs=self.x_coords, ys=self.y_coords, zs=self.z_values,
                                   linestyle="", marker=".")

    def start_pso_visualizer(self):
        self.pso.pop_initialisation()

        ani = animation.FuncAnimation(self.fig, self.update_3d_visualization, self.pso.generations_no,
                                      interval=1, blit=False, repeat=True, repeat_delay=5000)
        plt.show()
