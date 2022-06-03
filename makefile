SRC_DIR = src

JS_DIR = $(SRC_DIR)/js
PHP_DIR = $(SRC_DIR)/php
PY_DIR = $(SRC_DIR)/python

PY_ENV = $(PY_DIR)/venv
JS_DEPS = $(JS_DIR)/node_modules
PHP_VENDOR = $(PHP_DIR)/vendor

BOLD = \x1b[1m
RESET = \x1b[0m

# Prettify the output when lolcat is installed
_CAN_PRETTY := $(shell command -v lolcat)

ifeq (, $(_CAN_PRETTY))
    COLOR =
else
    COLOR = |lolcat
endif

all: fclean deps

# - Envs ---------------------------------------------------------------------------------------------------------------

$(PY_ENV):
	@ python -m venv $@
	@ chmod +x $@/bin/activate
	@ ./$@/bin/activate

# - Deps ---------------------------------------------------------------------------------------------------------------

PY_DEPS: $(PY_ENV)
	@ $^/bin/pip3 install -r $(PY_DIR)/requirements.txt

$(JS_DEPS):
	@ yarn install --cwd $(JS_DIR)

$(PHP_VENDOR):
	@ composer install -d $(PHP_DIR)

deps: $(PHP_VENDOR) $(JS_DEPS) PY_DEPS
	@ echo -e "$(BOLD)* All dependencies were installed$(RESET)" $(COLOR)

# - Readme -------------------------------------------------------------------------------------------------------------

docs/readme.md: $(PY_ENV)
	@ python -m scripts.auto_update_readme
	@ echo -e "$(BOLD)* Generated new readme.md$(RESET)" $(COLOR)

# - Tests --------------------------------------------------------------------------------------------------------------

js_test: $(JS_DEPS)
	@ yarn --cwd $(JS_DIR) test

php_test: $(PHP_VENDOR)
	@ $(PHP_VENDOR)/bin/phpunit --coverage-clover coverage.xml -c $(PHP_DIR)/phpunit.xml

py_test: PY_DEPS
	@ python -m pytest $(PY_DIR)/katas/*/*.py


# - Cleaning -----------------------------------------------------------------------------------------------------------

clean:
	@ rm -rf coverage.xml

	@ rm -rf htmlcov
	@ rm -rf $(JS_DIR)/coverage
	@ rm -rf .coverage

	@ rm -rf $(PHP_DIR)/coverage.xml
	@ rm -rf $(PHP_DIR)/.phpunit.result.cache
	@ rm -rf $(PHP_DIR)/.phpunit.cache

	@ rm -rf $(PY_DIR)/katas/*/.pytest_cache
	@ rm -rf .pytest_cache
	@ rm -rf .mypy_cache

	@ echo -e "$(BOLD)* cache cleaned up$(RESET)" $(COLOR)

fclean: clean
	@ rm -rf $(JS_DEPS)
	@ rm -rf $(PY_ENV)
	@ rm -rf $(PHP_DIR)/vendor
	@ echo -e "$(BOLD)* full clean done$(RESET)" $(COLOR)


.PHONY: PY_DEPS js_test php_test py_test fclean deps