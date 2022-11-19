start:
	python -m src.app

lint:
	python -m pylint src
	python -m pylint tests

test:
	python -m pytest tests

coverage:
	coverage run -m pytest tests
	coverage html