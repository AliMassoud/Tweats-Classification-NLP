from airflow.decorators import dag, task
from airflow.utils.dates import timedelta
from pendulum import today
import os
import pandas as pd
import shutil
import importlib.util
from pathlib import Path

@dag(
    dag_id="ingest_dag",
    description="ingest data from a file and store it in the DB",
    tags=["ingestion"],
    default_args={'owner': 'airflow'},
    schedule_interval=timedelta(minutes=2),
    start_date=today().add(hours=-1)
)
def ingest_dag():
    @task
    def store():
        my_files = os.listdir('Data/ingest_data/')
        if len(my_files) == 0:
            print("Directory is empty")
            return "Directory is empty"
        else:
            temp = ""
            for file in my_files:
                if os.path.isdir(file):
                    my_files.remove(file)
                else:
                    script_dir = Path( __file__ ).parent.parent
                    final_data_path = str(script_dir) + '/Data/ingest_data/' + file
                    temp = pd.read_csv(f'{final_data_path}')
                    # greate Expectations (2 expects)

                    
                    shutil.move(f"{final_data_path}", f"Data/data_for_dag_predict/{file}")
                    return
    # Task relationships
    store()

predict_dag = ingest_dag()