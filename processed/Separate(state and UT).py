import os
import shutil

source_dir="processed_Incidence_and_Rate_of_Suicides_yearly"
State_dir="processed_Incidence_and_Rate_of_Suicides_yearly/State_dir"
City_dir="processed_Incidence_and_Rate_of_Suicides_yearly/City_dir"

os.makedirs(State_dir,exist_ok=True)
os.makedirs(City_dir,exist_ok=True)

for file in os.listdir(source_dir):
    file_path=os.path.join(source_dir,file)

    if os.path.isfile(file_path):
        if 'table_1' in file.lower():
            shutil.move(file_path,os.path.join(State_dir,file))
            print(f"Moved from source_dir to State_dir:{file}")

        else:
            shutil.move(file_path,os.path.join(City_dir,file))
            print(f"Moved from source_dir to City_dir:{file}")
