
.PHONY: install
install:
	python -m pip install -U pip
	pip install -r requirements.txt
	pip install -e .

mypy:
	mypy .