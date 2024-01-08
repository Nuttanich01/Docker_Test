from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago 
import pandas as pd

if __name__ == '__main__':
    file = "/home/airflow/data/Transform_data.csv"
    raw = pd.read_csv(file)
    to_df = pd.DataFrame(raw)
    to_df.to_csv("/home/airflow/data/Real_data.csv", index=False)
    