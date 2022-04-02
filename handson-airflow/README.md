# Airflow

# Install airflow after creating a virtual environment
pip3 install apache_airflow==2.1.0 --constraint link_to_constraints

# Start the metastore and the files needed by airflow
airflow db init

# Start the webserver
airflow webserver

# Start the scheduler
airflow scheduler

# Create new user and its role
airflow users create -u admin -p admin -f Luiky -l Vasconcelos -r Admin -e admin@airflow.com

# List DAGs
airflow dags list

# List tasks of a DAG
airflow tasks list dag_id

# Test task
airflow tasks test dag_id task_id date_in_the_past
