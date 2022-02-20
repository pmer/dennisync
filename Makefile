.PHONY: init
init:
	pip install -r requirements.txt

.PHONY: init-34
init-34:
	pip install -r requirements-34.txt

.PHONY: format
format:
	black --quiet dennisync tests

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
