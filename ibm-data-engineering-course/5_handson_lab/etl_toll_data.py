"""
You have been assigned to a project that aims to de-congest the national highways
by analyzing the road traffic data from different toll plazas. Each highway is
operated by a different toll operator with a different IT setup that uses different
file formats. Your job is to collect data available in different formats and consolidate
it into a single file.
"""
import os
from datetime import datetime
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

#################### Configurations ####################
ROOT_FOLDER_PATH = os.path.join(
    "~",
    "Repositories",
    "courses-and-practices",
    "ibm-data-engineering-course",
    "5_handson_lab",
)
STAGING_FOLDER_PATH = os.path.join(
    ROOT_FOLDER_PATH,
    "staging",
)
DATA_FILE_NAME = "tolldata.tgz"
DATA_SOURCE_URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz"

#################### DAG ####################
# Defining DAG arguments
default_params = {
    "owner": "Luiky Vasconcelos",
    "start_date": datetime.utcnow(),
    "email": "luikymagno@gmail.com",
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Defining the DAG
dag = DAG(
    dag_id="etl_toll_data",
    description="Apache Airflow Final Assignment",
    doc_md=__doc__,
    default_args=default_params,
    schedule_interval=timedelta(days=1),
)

#################### Tasks ####################

download_data_task = BashOperator(
    task_id="download_data",
    bash_command=f"cd {STAGING_FOLDER_PATH} && wget -O {DATA_FILE_NAME} {DATA_SOURCE_URL}",
    dag=dag,
)

unzip_data_task = BashOperator(
    task_id="unzip_data",
    bash_command=f"cd {STAGING_FOLDER_PATH} && tar zxvf {DATA_FILE_NAME}",
    dag=dag,
)

extract_data_from_csv_task = BashOperator(
    task_id="extract_data_from_csv",
    bash_command=f"cd {STAGING_FOLDER_PATH} && cut -d',' -f1-4 vehicle-data.csv > csv_data.csv",
    dag=dag,
)

extract_data_from_tsv_task = BashOperator(
    task_id="extract_data_from_tsv",
    bash_command=f"cd {STAGING_FOLDER_PATH} && cut -f5-7 tollplaza-data.tsv | tr '\t' ',' > tsv_data.csv",
    dag=dag,
)

extract_data_from_fixed_width_task = BashOperator(
    task_id="extract_data_from_fixed_width",
    bash_command=f"cd {STAGING_FOLDER_PATH} && "
    + "awk '{print $(NF -1),$NF}' payment-data.txt | tr ' ' ',' > fixed_width_data.csv",
    dag=dag,
)

consolidate_data_task = BashOperator(
    task_id="consolidate_data",
    bash_command="paste csv_data.csv fixed_width_data.csv tsv_data.csv -d ',' > extracted_data.csv",
    dag=dag,
)

transform_data_task = BashOperator(
    task_id="transform_data",
    bash_command=f"cd {STAGING_FOLDER_PATH} && " + "awk '$4 = toupper($4)' extracted_data.csv > transformed_data.csv",
    dag=dag,
)

#################### DAG ####################
(
    download_data_task
    >> unzip_data_task
    >> extract_data_from_csv_task
    >> extract_data_from_tsv_task
    >> extract_data_from_fixed_width_task
    >> consolidate_data_task
    >> transform_data_task
)  # type: ignore
