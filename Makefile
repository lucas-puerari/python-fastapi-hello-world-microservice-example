COVERAGE_DIR = .coverage
COVERAGE_DATA_FILE = ${COVERAGE_DIR}/data
COVERAGE_HTML_DIR = $(COVERAGE_DIR)/html
COVERAGE_XML_FILE = ${COVERAGE_DIR}/xml

BADGES_DIR = .badges
COVERAGE_BADGE_FILE = ${BADGES_DIR}/coverage-badge.svg


start:
	python -m src.app

lint:
	python -m pylint src
	python -m pylint tests

test:
	python -m pytest tests

coverage:
	coverage run --data-file ${COVERAGE_DATA_FILE} -m pytest tests
	coverage html --data-file ${COVERAGE_DATA_FILE} -d ${COVERAGE_HTML_DIR}
	coverage xml --data-file ${COVERAGE_DATA_FILE} -o ${COVERAGE_XML_FILE}
	genbadge coverage -i ${COVERAGE_XML_FILE} -o ${COVERAGE_BADGE_FILE}