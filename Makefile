.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' \
	| sort

.PHONY: package
package: ## build packages
	poetry build

.PHONE: release-test
release-test: ## release packages to testpypi
	poetry publish -r testpypi --build

.PHONY: release-prod
release-prod: ## release packages to pypi
	poetry publish -r pypi --build

.PHONY: clear-dist
clear-dist: ## clear package files
	@-rm -rf dist/*

.PHONY: test
test: ## run tests
	tox
