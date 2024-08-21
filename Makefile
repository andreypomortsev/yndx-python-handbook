setup:
	python3 -m venv .venv
	@echo "\n\033[0;31mНе забудьте активировать виртуальную среду перед установкой библиотек!\033[0m\n"

install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black . --line-length=79 && isort .

lint:
	flake8 .

test: lint test-21 test-22 test-23 test-24 test-31 test-32 test-33 test-34

test-html:
	pytest --cov-report=html

test-xml:
	pytest --cov-report=xml

test-21:
	pytest tests/2.1/

test-22:
	pytest tests/2.2/

test-23:
	pytest tests/2.3/

test-24:
	pytest tests/2.4/

test-31:
	pytest tests/3.1/

test-32:
	pytest tests/3.2/

test-33:
	pytest tests/3.3/

test-34:
	pytest tests/3.4/

debug:
	pytest -vv