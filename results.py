import pickle
import pandas as pd

class Results():
    def __init__(self):
        self.df = pd.DataFrame(columns = ["Function", "Inertia", "Cognitive", "Social", "Max_velocity", "Pop_size", "Generation_no", "Function_dimensions", "Min", "Max", "Mean"])
    
    def add(self, function_name, constants, min_val, max_val, mean_val, generation_index = None):
        if generation_index == None:
            generation_index = constants.GENERATIONS_NO

        self.df = self.df.append({
            "Function" : function_name,
            "Inertia" : constants.INERTIA_WEIGHT,
            "Cognitive": constants.COGNITIVE_WEIGHT,
            "Social": constants.SOCIAL_WEIGHT,
            "Max_velocity": constants.MAX_VELOCITY_ALLOWED,
            "Pop_size": constants.POP_SIZE,
            "Generation_no": generation_index,
            "Function_dimensions": constants.DIMENSIONS_OF_THE_FUNCTION,
            "Min": min_val,
            "Max": max_val,
            "Mean": mean_val
        }, ignore_index = True)
    
    def save(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self.df, f)
    
    def load(self, filename):
        with open(filename, "rb") as f:
            self.df = pickle.load(f)