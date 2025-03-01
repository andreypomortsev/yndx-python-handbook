setup:
	pip3 install poetry -q
	poetry install
	poetry shell

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	find ../. -name '.coverage' -delete

format:
	poetry run black . --line-length=79 && poetry run isort .

lint:
	poetry run flake8 .

test: lint
	poetry run pytest -n auto; $(MAKE) clean

test-dir-%:
	poetry run pytest -n auto tests/$*/; $(MAKE) clean

test-file-%:
	./fileTest.sh $*; $(MAKE) clean

test-report-%:
	poetry run pytest -n auto --cov-report=$*; $(MAKE) clean

debug:
	poetry run pytest -n auto -vv; $(MAKE) clean
