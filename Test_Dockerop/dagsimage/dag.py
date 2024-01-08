from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago 
from airflow.providers.docker.operators.docker import DockerOperator

with DAG(
        dag_id='test_dockerop',
        start_date=days_ago(0),
        schedule_interval="@daily",
        tags=["Test"]
) as dag:
    

    task1 = DockerOperator(
        task_id='run_e',
        image='e:3',
        api_version='auto',
        network_mode="bridge",
        #docker_url="unix://var/run/docker.sock",
        # volumes=["test_dockop_data_path:/home/airflow/data"],
        docker_url='tcp://docker-proxy:2375',
        command='python3 /opt/airflow/dags/extract.py',
    )
    task2 =  DockerOperator(
        task_id='run_t',
        image='t:3',
        api_version='auto',
        network_mode="bridge",
        #docker_url="unix://var/run/docker.sock",
        # volumes=["test_dockop_data_path:/home/airflow/data"],
        docker_url='tcp://docker-proxy:2375',
        command='python3 /opt/airflow/dags/transforms.py',
    )
    task3 =  DockerOperator(
        task_id='run_l',
        image='l:3',
        api_version='auto',
        network_mode="bridge",
        #docker_url="unix://var/run/docker.sock",
        #volumes=["../data:/home/airflow/data"],
        docker_url='tcp://docker-proxy:2375',
        command='python3 /opt/airflow/dags/load.py',
    ) 

    task1 >> task2 >> task3 