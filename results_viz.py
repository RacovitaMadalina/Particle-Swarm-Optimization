import pandas as pd

from results import Results
from constants import results_file

results = Results()
results.load(results_file)

pd.set_option("display.max_rows", len(results.df))

print(results.df)