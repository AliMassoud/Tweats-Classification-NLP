from airflow.decorators import dag, task
from airflow.utils.dates import timedelta
from pendulum import today
from My_Predict_Job_functions import ingest_file
import sys
sys.path.append("/mnt/c/Users/user/Desktop/DSP_Project_APIs/APIs_Flask/Backend_APIs/Services")

from predictionFunction import predicted_outcome
from save_output_Files import save_data

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
    def get_data_to_ingest_from_local_file_task():
        return ingest_file()

    @task
    def predict(data_to_ingest_df):
        return predicted_outcome(data_to_ingest_df)

    @task
    def save_data_task(data_to_ingest_df):
        save_data(data_to_ingest_df)

    # Task relationships
    data_to_ingest = get_data_to_ingest_from_local_file_task()
    if(type(data_to_ingest) != 'str'):  
        df = predict(data_to_ingest)
        save_data_task(df)




ingest_data_dag = ingest_data()




