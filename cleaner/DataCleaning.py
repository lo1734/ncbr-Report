import os

import pandas as pd

#table_1 for States
#table_2 for Cities

csv_folder="../processed/processed_Incidence_and_Rate_of_Suicides_yearly"
cleaned_folder="../cleaner/cleaned_data"
os.makedirs(cleaned_folder,exist_ok=True)

for file in os.listdir(csv_folder):
    if 'table_1' in file:
        df_states

