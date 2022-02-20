.PHONY: init
init:
	pip install -r requirements.txt

.PHONY: lint
lint:
	pylint dennisync tests

.PHONY: test
test:
	pytest

.PHONY: coverage
coverage:
	coverage run -m pytest
	coverage lcov
	coverage report -m
