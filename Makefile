.PHONY: init
init:
	pip install -r requirements.txt

.PHONY: test
test:
	pytest --verbose

.PHONY: coverage
coverage:
	pytest --cov=dennisync

.PHONY: ci
ci:
	coverage run --source=dennisync -m pytest

.PHONY: coveralls
coveralls:
	coveralls

.PHONY: flake8
flake8:
	flake8 dennisync
