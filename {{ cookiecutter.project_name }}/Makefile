.DEFAULT_GOAL := help

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: clean
clean: clean_pyc clean_pycache ## Clean all PYC in the system

.PHONY: clean_pyc
clean_pyc: ## Cleans all *.pyc in the system
	find . -type f -name "*.pyc" -delete || true

.PHONY: clean_pycache
clean_pycache: ## Removes the __pycaches__
	find . -type d -name "*__pycache__*" -delete

.PHONY: run
run: ## Starts the local server with production settings
	ESMERALD_SETTINGS_MODULE={{ cookiecutter.project_name }}.configs.development.settings.DevelopmentAppSettings python -m {{ cookiecutter.project_name }}.serve

.PHONY: migrate
migrate: ## Runs the all the migrations
	aerich migrate

.PHONY: migrate-specific
migrate-specific: ## Migrates to specific file
	aerich migrate --name $(FILE)

.PHONY: upgrade
upgrade: ## Upgrade to latest version (migrates as well)
	aerich upgrade

.PHONY: downgrade
downgrade: ## Downgrade to specified version. E.g.: aerich downgrade -v VERSION=1
	aerich downgrade -v $(VERSION)

.PHONY: requirements
requirements: ## Starts the local server with production settings
	pip install -r requirements/development.txt

.PHONY: test
test: ## Runs the local tests with nose
	ESMERALD_SETTINGS_MODULE={{ cookiecutter.project_name }}.configs.testing.settings.TestingAppSettings pytest -s $(TESTONLY)


ifndef VERBOSE
.SILENT:
endif
