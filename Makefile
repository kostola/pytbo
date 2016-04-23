.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  bdist          to build wheel universal binary distribution"
	@echo "  clean          to clean build artifacts"
	@echo "  register       to register the package to PyPI"
	@echo "  register-test  to register the package to PyPI Test"
	@echo "  sdist          to build source distribution"
	@echo "  upload         to upload ALL the current built distributions to PyPI"
	@echo "  upload-test    to upload ALL the current built distributions to PyPI Test"

.PHONY: bdist
bdist:
	python setup.py bdist_wheel --universal

.PHONY: clean
clean:
	rm -fr build dist .egg pytbo.egg-info

.PHONY: init
init:
	pip install -r requirements.txt

.PHONY: register
register:
	twine register dist/*

.PHONY: register
register-test:
	twine register -r pypitest dist/*

.PHONY: sdist
sdist:
	python setup.py sdist

.PHONY: upload
upload:
	twine upload dist/*

.PHONY: upload
upload-test:
	twine upload -r pypitest dist/*
