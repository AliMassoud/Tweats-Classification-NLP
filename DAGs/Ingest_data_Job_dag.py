from airflow.decorators import dag, task
from airflow.utils.dates import timedelta
from pendulum import today
import pandas as pd
from My_Predict_Job_functions import ingest_file
import requests
import os
import shutil
# from src.Backend_APIs.Others.Services.predictionFunction import predicted_outcome
# from src.Backend_APIs.Others.Services.save_output_Files import save_data
# src\Backend_APIs\Others\Services\predictionFunction.py
@dag(
    dag_id="ingest_data_2",
    description="Ingest data from a file the model",
    tags=["example"],
    default_args={'owner': 'airflow'},
    schedule_interval=timedelta(minutes=1),
    start_date=today().add(hours=-1)
)
def ingest_data():
    @task
    def predict():
        # Ingestion_predition_folder = "Data/Data_Ingestion/"
        my_files = os.listdir('Data/Data_Ingestion/')
        os.chdir('Data/Data_Ingestion/')
        if len(my_files) == 0:
            print("Directory is empty")
            return "Directory is empty"
        else:
            temp = ""
            for file in my_files:
                if os.path.isdir(file):
                    my_files.remove(file)
                else:
                    temp = file
                    print(temp)
                    f =  open(f'{temp}','rb')
                    files = {"data_file": f}
                    res = requests.get("http://127.0.0.1:5000/SubmitFile", files=files)
                    shutil.move(f"{temp}", f"../Moved_Data_Files/{temp}")
                    return

    # Task relationships
    predict()



ingest_data_dag = ingest_data()




