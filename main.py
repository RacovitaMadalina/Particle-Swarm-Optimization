from functions_to_be_minimized import *
from visualization import *
from experiment_utils import Experiment
from constants import Constants, results_file
from results import Results

if __name__ == '__main__':

    # without visualisation
    # pso = PSO(de_jong)
    # pso.solve_pso_problem()

    # with visualisation
    # visualiser = PSOVisualization(griewangk)
    # visualiser.start_pso_visualizer()

    constants = Constants()

    # experiment = Experiment(griewangk, constants)
    # max_value, min_value, mean_value = experiment.run_experiment(30)
    # print('Min = ', min_value, " Max = ", max_value, " Mean = ", mean_value)
    # exit(0)

    GET_WEIGHTS = True

    results = Results()
    results.load(results_file)

    if GET_WEIGHTS == True:
        # Get best combination of weights
        inertia_weights = [0.5, 0.8, 1]
        cognitive_weights = [0.5, 1, 2.05, 4]
        social_weights = [0.5, 1, 2.05, 4]

        for inertia_weight in inertia_weights:
            for cognitive_weight in cognitive_weights:
                for social_weight in social_weights:
                    constants.INERTIA_WEIGHT = inertia_weight
                    constants.COGNITIVE_WEIGHT = cognitive_weight
                    constants.SOCIAL_WEIGHT = social_weight

                    print(inertia_weight, cognitive_weight, social_weight)
                    # 30 experiments on a fixed population + statistics
                    experiment = Experiment(griewangk, constants)
                    max_value, min_value, mean_value = experiment.run_experiment(30)
                    print('Min = ', min_value, " Max = ", max_value, " Mean = ", mean_value)

                    results.add("griewangk", constants, min_value, max_value, mean_value)
    else:
        weight_combinations = [(0.5, 0.50, 4.00), (0.5, 4.00, 1.00), (0.5, 1.00, 4.00), (0.8, 1.00, 1.00)]
        
        for (inertia_weight, cognitive_weight, social_weight) in weight_combinations:
            constants.INERTIA_WEIGHT = inertia_weight
            constants.COGNITIVE_WEIGHT = cognitive_weight
            constants.SOCIAL_WEIGHT = social_weight

            print(inertia_weight, cognitive_weight, social_weight)
            # 30 experiments on a fixed population + statistics
            experiment = Experiment(rastrigin, constants)
            max_value, min_value, mean_value = experiment.run_experiment(1, results)
            print('Min = ', min_value, " Max = ", max_value, " Mean = ", mean_value)

            #results.add("rastrigin", constants, min_value, max_value, mean_value)

    results.save(results_file)