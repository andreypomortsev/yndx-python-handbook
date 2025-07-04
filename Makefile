# Colors for output
GREEN := \033[0;32m
NC := \033[0m # No Color

.PHONY: setup clean format lint test test-dir test-file test-report debug help

help: ## Show this help message
	@echo "Available targets:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

setup: ## Install dependencies and setup environment
	pip3 install poetry -q
	poetry install

clean: ## Remove Python cache and coverage files
	@echo "$(GREEN)Cleaning up...$(NC)"
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name ".coverage" -delete
	find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "coverage.xml" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true

format: ## Format code with black and isort
	poetry run black . --line-length=79
	poetry run isort .

lint: ## Run linting with flake8
	poetry run flake8 .

test: lint ## Run tests after linting
	poetry run pytest -n auto
	$(MAKE) clean

test-dir-%: ## Run tests for specific directory (usage: make test-dir-chapter1)
	@test -d tests/$* || (echo "Directory tests/$* does not exist" && exit 1)
	poetry run pytest -n auto tests/$*/
	$(MAKE) clean

test-file-%: ## Run tests for specific file (usage: make test-file-test_something)
	@test -f ./fileTest.sh || (echo "fileTest.sh script not found" && exit 1)
	./fileTest.sh $*
	$(MAKE) clean

test-report-%: ## Generate test coverage report (usage: make test-report-html)
	poetry run pytest -n auto --cov=. --cov-report=$*
	$(MAKE) clean

debug: ## Run tests in debug mode with verbose output
	poetry run pytest -n auto -vv
	$(MAKE) clean

ci: lint test ## Run CI pipeline (lint + test)

dev-shell: ## Activate poetry shell for development
	poetry shell