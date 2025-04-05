# Setup and Pre-requisites

The project use Airflow on docker. Airflow already configured on Dockerfile and docker-compose.yaml. 

If you already have Docker installed and running then no further installation required. Configuring docker files is out of the scope of this class.

Go through the following command prompts to initiate Airflow on Docker

### On Window (Command prompts)
Make sure you're at the project lab directory

```Shell
mkdir logs
mkdir plugins
mkdir configs
set AIRFLOW_UID=50000

docker compose up airflow-init
docker compose up
```

Then go to `localhost:8080` on your browser and sign in with username=airflow and password=airflow
If you can see Airflow UI with 2 dags then your set up is successful


### On Mac/Linux
```Bash
mkdir -p ./dags ./logs ./plugins ./config
export AIRFLOW_UID=$(id -u)

docker compose up airflow-init
docker compose up
```
Then go to `localhost:8080` on your browser and sign in with username=airflow and password=airflow
If you can see Airflow UI with 2 dags then your set up is successful


### Working on Airflow Docker environment

You can make changes to your dags code when the docker container is running. It will parse your 
codes and update the UI momentarily as soon as you save it. Unless you need to update Airflow configs, 
plugins, package providers (which you don't for this lab), there's no need to restart the container.

To exit the container. Either Cmd/Ctrl+C on your terminal or stop it from your Docker Desktop UI.

