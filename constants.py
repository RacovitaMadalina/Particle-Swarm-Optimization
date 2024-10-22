
results_file = "results/rastrigin.pickle"

class Constants():
	def __init__(self):
		self.PRECISION = 9

		# establish the balance between exploration and exploitation
		self.INERTIA_WEIGHT = 0.5

		# tendency of duplicating past self actions which were proven to be successful
		self.COGNITIVE_WEIGHT = 0.5

		# tendency of following collective success (i.e. success of other individuals)
		self.SOCIAL_WEIGHT = 4

		# lowers the ability of exploration by reducing the velocity to a given limit value
		self.MAX_VELOCITY_ALLOWED = 1

		self.POP_SIZE = 250
		self.GENERATIONS_NO = 700
		self.DIMENSIONS_OF_THE_FUNCTION = 30

		self.INTERVALS_OF_DEFINITION = {
		    'quadric_function': [-10, 10],
		    'de_jong': [-5.12, 5.12],
		    'six_hump_camel_back': [-3, 3],
		    'rosenbrock': [-2.048, 2.048],
		    'rastrigin': [-5.12, 5.12],
		    'griewangk': [-600, 600]
		}
