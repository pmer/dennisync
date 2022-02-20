.PHONY: init
init:
	pip install -r requirements.txt

.PHONY: test
test:
	pytest --verbose

.PHONY: coverage
coverage:
	pytest --cov-report=term --cov-report=xml --cov=dennisync

.PHONY: flake8
flake8:
	flake8 dennisync
