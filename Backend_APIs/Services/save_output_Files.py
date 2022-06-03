from datetime import datetime

def save_data(data_to_ingest_df):
    filepath = f"output_data/{datetime.now()}.csv"
    data_to_ingest_df.to_csv(filepath, index=False)