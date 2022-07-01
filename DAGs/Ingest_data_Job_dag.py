from airflow.decorators import dag, task
from airflow.utils.dates import timedelta
from pendulum import today
import os
import pandas as pd
import shutil
from pathlib import Path
import great_expectations as ge

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
                    # temp = ge.read_csv(f'{final_data_path}')
                    
                    df = ge.read_csv(f'{final_data_path}')
                    https = df.expect_column_values_to_not_match_regex('text', "http\S+")
                    tags = df.expect_column_values_to_not_match_regex('text', '@[^\s]+')
                    hashtags = df.expect_column_values_to_not_match_regex('text', '#[^\s]+')
                    print(hashtags)
                    if hashtags.success is True:
                        print("No hashtags in our data")
                    else:
                        df['text'] = df['text'].str.replace(r'#[^\s]+', '').str.strip()

                    if tags.success is True:
                        print("No Tags in our Data!")             
                    else:
                        df['text'] = df['text'].str.replace(r'@[^\s]+', '').str.strip()

                    if https.success is True:
                        print("No HTTPs Links in our data!")
                    else:
                        df['text'] = df['text'].str.replace(r'http\S+', '').str.strip()

                    temp = pd.DataFrame(df)
                    temp.to_csv(f"Data/data_for_dag_predict/{file}")
                    shutil.move(f"{final_data_path}", f"Data/moved_original_data_from_Ingestion/{file}")
                    return
    # Task relationships
    store()

predict_dag = ingest_dag()