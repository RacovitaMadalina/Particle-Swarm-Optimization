PRECISION = 9

# establish the balance between exploration and exploitation
INERTIA_WEIGHT = 0.8

# tendency of duplicating past self actions which were proven to be successful
COGNITIVE_WEIGHT = 1

# tendency of following collective success (i.e. success of other individuals)
SOCIAL_WEIGHT = 1

# lowers the ability of exploration by reducing the velocity to a given limit value
MAX_VELOCITY_ALLOWED = 300

POP_SIZE = 100
GENERATIONS_NO = 1000
DIMENSIONS_OF_THE_FUNCTION = 10

INTERVALS_OF_DEFINITION = {
    'quadric_function': [-10, 10],
    'de_jong': [-5.12, 5.12],
    'six_hump_camel_back': [-3, 3],
    'rosenbrock': [-2.048, 2.048],
    'rastrigin': [-5.12, 5.12],
    'griewangk': [-600, 600]
}
