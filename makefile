venv:
ve:
	python3 -mvenv venv
	@echo upgrading pip, setuptools, build, wheel
	@venv/bin/pip install --quiet --upgrade pip setuptools build wheel
	@echo installing poetry
	@venv/bin/pip install --quiet poetry
	poetry install --no-root

clean:
	rm -rf venv

app:
	source venv/bin/activate && python3 setup.py py2app
