.PHONY: setup
setup:
	( \
		python3 -m venv venv; \
		. venv/bin/activate; \
		pip3 install --upgrade pip; \
		pip3 install -r requirements.txt; \
	)

.PHONY: clean-setup
clean:
	rm -rf venv

.PHONY: ingest
ingest:
	docker-compose up

.PHONY: clean-ingest
clean-ingest:
	docker-compose down