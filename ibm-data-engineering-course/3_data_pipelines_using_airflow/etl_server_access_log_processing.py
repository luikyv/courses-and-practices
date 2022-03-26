#################### Import libraries ####################
import os
from datetime import datetime
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

#################### DAG arguments ####################

RAW_DATA_FILE_NAME = "web-server-access-log.txt"
RAW_DATA_SOURCE_URL = f"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Build%20a%20DAG%20using%20Airflow/{RAW_DATA_FILE_NAME}"
RAW_DATA_FOLDER_PATH = "~/Repositories/ibm-data-engineering-course/3_data_pipelines_using_airflow/raw_data/"
DATA_FOLDER_PATH = "~/Repositories/ibm-data-engineering-course/3_data_pipelines_using_airflow/data/"

defaults = {
    "author": "Luiky Vasconcelos",
    "start_date": datetime.utcnow(),
    "retries": 1,
    "retry_delay": timedelta(seconds=5),
}

#################### Defining the DAG ####################

dag = DAG(
    dag_id="etl_server_access_log_processing",
    default_args=defaults,
    description="Extract logs from a web server, clean and filter them, and load them to a .csv",
    schedule_interval=timedelta(seconds=10),
)

#################### Defining the tasks ####################

download_task = BashOperator(
    task_id="download",
    bash_command=f"wget -O {os.path.join(RAW_DATA_FOLDER_PATH, RAW_DATA_FILE_NAME)} {RAW_DATA_SOURCE_URL}",
    dag=dag,
)

# Extract fields timestamp and visitorid which are separed by '#'
RAW_EXTRACTED_DATA_FILE_NAME = "extracted_" + RAW_DATA_FILE_NAME.replace("-", "_")
extract_task = BashOperator(
    task_id="extract",
    bash_command=f"cut -d# -f1,4 {os.path.join(RAW_DATA_FOLDER_PATH, RAW_DATA_FILE_NAME)} > {os.path.join(RAW_DATA_FOLDER_PATH, RAW_EXTRACTED_DATA_FILE_NAME)}",
    dag=dag,
)

# Capitalize the visitorid and put the content in the csv format
TRANSFORMED_DATA_FILE_NAME = "tranformed_log_data.csv"
transform_task = BashOperator(
    task_id="transform",
    bash_command=f"tr '[a-z]' '[A-Z]' < {os.path.join(RAW_DATA_FOLDER_PATH, RAW_EXTRACTED_DATA_FILE_NAME)} | tr '#' ',' > {os.path.join(DATA_FOLDER_PATH, TRANSFORMED_DATA_FILE_NAME)}",
    dag=dag,
)

# Zip the tranformed data
load_task = BashOperator(
    task_id="load",
    bash_command=f"cd {DATA_FOLDER_PATH} && zip {TRANSFORMED_DATA_FILE_NAME.replace('.csv', '.zip')} {TRANSFORMED_DATA_FILE_NAME}",
    dag=dag,
)

#################### Task pipeline ####################
download_task >> extract_task >> transform_task >> load_task  # type: ignore
