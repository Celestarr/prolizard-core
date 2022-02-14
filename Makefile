reset:
	@docker-compose down -v --remove-orphans

check: ## Check source code issues
	black --diff --check .
	isort --diff --check .
	bandit -r . --configfile pyproject.toml
	flake8 .
	find . -iname "*.py" -not -path "./venv/*" -not -path "*/migrations/*" -not -path "*/node_modules/*" | xargs pylint
	python manage.py makemigrations --dry-run --check

deps: ## Install dependencies
	pip install -r requirements.txt

fmt: ## Format code
	black .
	isort --atomic .

test: ## Run tests
	python manage.py test

help: ## Show this help
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} { \
		if (/^[a-zA-Z_-]+:.*?##.*$$/) {printf "    %-20s%s\n", $$1, $$2} \
		else if (/^## .*$$/) {printf "  %s\n", substr($$1,4)} \
		}' $(MAKEFILE_LIST)
