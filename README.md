# Airflow Data Ingestion

Airflow running on LocalExecutor started up by docker-compose.

Purpose of this project is to learn the concepts of airflow as well as its capabilities.

This project can also serve as a template to expand on in the future to play with different types of Executors on Airflow

# Prerequisite

Before we begin, there are a few tools needed to run the project

1. Python
2. Make
3. Docker
4. Docker Compose

# Setting up

After cloning the repo, navigate into the root directory of the repo.

In the root directory, run the following command to setup a python virtual environment and directories needed for Airflow to run locally.

After the setup, activate the virtual environment.

```
make setup
source venv/bin/activate
```

Next, we need to create an `.env` file and populate it with some environment variables.

```.env
# Airflow config
AIRFLOW__CORE__EXECUTOR=LocalExecutor
AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql://airflow:airflow@postgres/airflow
AIRFLOW__CORE__DAGS_ARE_PAUSED_AT_CREATION=true
AIRFLOW__CORE__LOAD_EXAMPLES=false
AIRFLOW_UID=50000
```

The `.env` file is needed inside the `compose.yaml` file.  

After creating the `.env` file, run `make up` to start airflow locally.

To login into airflow, enter `http://localhost:8080` into your browser.  
```airflow username & password
Username: admin
Password: admin
```

Once we're done with running Airflow locally, we can run this `make down` to remove the containers, and 
directories needed for Airflow to run

* Note
Navigate to the `Makefile`, and remove the `make reset` command inside 
the `Makefile.down` section to preserve the airflow data for the next local run.

To clean up the virtual environment & airflow data directories created during setup, 
run `make clean-setup`

# Contribution guidelines

1. Each contribution should be in a separate branch
2. A Pull Request (PR) will be created to merge changes into the master branch
3. Each Pull Request (PR) title will need to have the one of the
   following prefix

```
- feat:     A new feature
- fix:      A bug fix
- docs:     Documentation only changes
- style:    Formatting, missing semi-colons, white-space, etc
- refactor: A code change that neither fixes a bug nor adds a feature
- perf:     A code change that improves performance
- test:     Adding missing tests
- chore:    Maintain. Changes to the build process or auxiliary tools/libraries/documentation
```
