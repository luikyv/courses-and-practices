"""
To submit the dag created in this script you must make a copy of it in your airflow/dags
You can do so with: "mkdir -p ~/airflow/dags && cp 3_data_pipelines_using_airflow/my_first_dag.py ~/airflow/dags/"

About updating DAGs: https://cloud.google.com/composer/docs/how-to/using/managing-dags
"""
#################### Import libraries ####################
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

# The DAG object; we'll need this to instantiate a DAG
# Operators; we need this to write tasks!
# This makes scheduling easy

#################### Defining general arguments ####################
RAW_DATA_FILE_PATH = (
    "~/Repositories/ibm-data-engineering-course/3_data_pipelines_using_airflow/raw_data/extracted_data.txt"
)
DATA_FILE_PATH = "~/Repositories/ibm-data-engineering-course/3_data_pipelines_using_airflow/data/transformed_data.csv"

#################### Defining DAG arguments ####################

# You can override them on a per-task basis during operator initialization
default_args = {
    "owner": "Luiky Vasconcelos",
    "start_date": days_ago(0),
    "email": ["luikymagno@gmail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(seconds=5),
}

#################### Defining the DAG ####################

dag = DAG(
    dag_id="my_first_dag",
    default_args=default_args,
    description="My first DAG",
    schedule_interval=timedelta(seconds=5),
)

#################### Defining the tasks ####################

########## First task ##########
extract_task = BashOperator(
    task_id="extract",
    bash_command=f"cut -d':' -f1,3,6 /etc/passwd > {RAW_DATA_FILE_PATH}",
    dag=dag,
)

########## Second task ##########
tranform_and_load_task = BashOperator(
    task_id="tranform_and_load",
    bash_command=f"tr ':' ',' < {RAW_DATA_FILE_PATH} > {DATA_FILE_PATH}",
    dag=dag,
)

#################### Task pipeline ####################
extract_task >> tranform_and_load_task  # type: ignore
