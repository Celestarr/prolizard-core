reset:
	@docker-compose down -v --remove-orphans

check: ## Check source code issues
	black --diff --check .
	isort --diff --check .
	bandit --recursive ./app ./dev ./docker --configfile .bandit.yml
	flake8 .
	pylint app dev docker

deps: ## Install dependencies
	pip install -r requirements.txt

fmt: ## Format code
	black .
	isort --atomic .

test: check ## Run tests
	git status -s

help: ## Show this help
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} { \
		if (/^[a-zA-Z_-]+:.*?##.*$$/) {printf "    %-20s%s\n", $$1, $$2} \
		else if (/^## .*$$/) {printf "  %s\n", substr($$1,4)} \
		}' $(MAKEFILE_LIST)
