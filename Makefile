VENV_DIR := venv
VENV := . venv/bin/activate
SOURCE_DIRS := yajl

.PHONY: venv clean lint

clean:
	rm -rf $(VENV_DIR)

venv:
	python3.8 -m venv $(VENV_DIR)
	$(VENV); pip3 install --upgrade pip
	$(VENV); pip3 install -r requirements.txt

lint: venv
	$(VENV); mypy --strict  $(SOURCE_DIRS)
	$(VENV); pylint $(SOURCE_DIRS)
	$(VENV); black --check $(SOURCE_DIRS)

format: venv
	$(VENV); black $(SOURCE_DIRS)
