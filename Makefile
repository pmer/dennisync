.PHONY: init
init:
	pip install -r requirements.txt

.PHONY: test
test:
	pytest

.PHONY: ci
ci:
	pytest --junitxml=report.xml

.PHONY: coverage
coverage:
	pytest --cov-config .coveragerc --verbose --cov-report term --cov-report xml --cov=dennisync

.PHONY: flake8
flake8:
	flake8 dennisync
