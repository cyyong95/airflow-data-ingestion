# Simple Data Ingestion

The python script is created to ingest a parquet file from a URL specified in
an environment file, and populate a Postgresql database.  

The whole process is run on containers.

## Prerequisite
Before we begin, there are a few tools that are needed to run the project
1. Python
2. Make
3. Docker
4. Docker Compose

## Steps to run the project
### Environment file setup
The project has been setup to run in a few steps:  
First we create a `.env` file with the following variables and fill in the values
```
HOST_PORT=<host_port>
HOST_VOLUME_DIR=<directory_to_save_database_state>
DATABASE_CONTAINER_NAME=<database_container_name>
CONTAINER_PORT=<container_port>
POSTGRES_USER=<database_username>
POSTGRES_PASSWORD=<database_password>
POSTGRES_DB=<database_name>
POSTGRES_TABLE_NAME=<database_table_name>
DATASET_PARQUET=<text_file_parquet/url_to_parquet_file>
```

After creating the `.env` file, we just need to run the command
```
make ingest
```

Running this command will build the containers, and run the script will
read the parquet file or download a parquet file from a specified URL,
and start ingesting the first 100 records.

### Running the script locally
In order to run the script locally, we will need to run this command
```
# initialize a virtual environment
make setup

# activate the virtual environment
source venv/bin/activate
```

After activating the virtual environment, we'll have to manually build
the `Dockerfile`, and run the image with an existing database container in
the same docker network.

## Contribution guidelines
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