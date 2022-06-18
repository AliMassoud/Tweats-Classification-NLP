import os
import shutil
import pandas as pd


Ingestion_predition_folder = "Data/Data_Ingestion/"
#####
def ingest_file():
    my_files = os.listdir("Data/Data_Ingestion/")
    num_files = 0
    os.chdir('Data/Data_Ingestion/')
    if len(my_files) == 0:
        print("Directory is empty")
        return "Directory is empty"
    else:
        temp = ""
        for file in my_files:
            # num_files = num_files + 1
            # if(num_files != 4):
            if os.path.isdir(file):
                my_files.remove(file)
            else:
                temp = file
                data = pd.read_csv(file, encoding= 'unicode_escape')
                shutil.move(f"{temp}", f"../Moved_Data_Files/{temp}")
                return data
            # else:
    # return

        