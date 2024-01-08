FROM python:3.9


WORKDIR /home/airflow/data
# Copy the DAG files from the host machine to the image
COPY . /opt/airflow/dags/

RUN pip install -r /opt/airflow/dags/requirements.txt

# Set the entrypoint command
#CMD [ "docker", "run", "-v" ,"../data:/home/airflow/data" , "e:2"]