# from DAGs.My_Predict_Job_functions import ingest_file

# ingest_file()

from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv('.env'))

print(os.getenv('DB_NAME'))