setup:
	python3 -m venv .venv
	@echo "\n\033[0;31mНе забудьте активировать виртуальную среду перед установкой библиотек!\033[0m\n"

install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black . --line-length=79 && isort .

lint:
	flake8 .

test: lint 
	pytest

test-dir-%:
	pytest tests/$*/

test-file-%:
	./fileTest.sh $*

test-report-%:
	pytest --cov-report=$*

debug:
	pytest -vv
