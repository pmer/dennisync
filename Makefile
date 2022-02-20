.PHONY: init
init:
	pip install -r requirements.txt

.PHONY: flake8
flake8:
	flake8 dennisync

.PHONY: test
test:
	pytest --verbose

.PHONY: coverage
coverage:
	coverage run -m pytest
	coverage lcov
	coverage report -m
