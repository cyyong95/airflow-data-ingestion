.PHONY: setup
setup:
	( \
		python3 -m venv venv; \
		. venv/bin/activate; \
		pip3 install --upgrade pip; \
		pip3 install -r requirements.txt; \
		mkdir airflow/logs && mkdir airflow/airflow_pg_data; \
	)

.PHONY: clean-setup
clean-setup:
	rm -rf venv
	rm -rf airflow/logs
	rm -rf airflow/airflow_pg_data

.PHONY: reset
reset:
	rm -rf airflow/logs
	rm -rf airflow/airflow_pg_data
	mkdir airflow/logs
	mkdir airflow/airflow_pg_data

.PHONY: up
up:
	docker-compose -f compose.yaml up --build

.PHONY: down
down:
	docker-compose -f compose.yaml down
	make reset