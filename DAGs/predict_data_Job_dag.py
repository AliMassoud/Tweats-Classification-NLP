from airflow.decorators import dag, task
from airflow.utils.dates import timedelta
from pendulum import today
import requests
import os
import shutil
@dag(
    dag_id="prediction_dag",
    description="predict data from a file and send to the model then store in the DB",
    tags=["prediction"],
    default_args={'owner': 'airflow'},
    schedule_interval=timedelta(minutes=2),
    start_date=today().add(hours=-1)
)
def prediction_dag():
    @task
    def predict():
        my_files = os.listdir('Data/data_for_dag_predict/')
        os.chdir('Data/data_for_dag_predict/')
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
                    shutil.move(f"{temp}", f"../Moved_Data_Files_Predict/{temp}")
                    return

    # Task relationships
    predict()



predict_dag = prediction_dag()




