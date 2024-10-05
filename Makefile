setup:
	pip3 install poetry -q
	poetry install
	poetry shell

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

format:
	poetry run black . --line-length=79 && poetry run isort .

lint:
	poetry run flake8 .

test: lint 
	poetry run pytest || true
	@$(MAKE) clean -q

test-dir-%:
	poetry run pytest tests/$*/ || true
	@$(MAKE) clean -q

test-file-%:
	poetry run ./fileTest.sh $* || true
	@$(MAKE) clean -q

test-report-%:
	poetry run pytest --cov-report=$* || true
	@$(MAKE) clean -q

debug:
	poetry run pytest -vv || true
	@$(MAKE) clean -q
