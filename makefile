venv:
ve:
	python3 -mvenv venv
	@echo upgrading pip, setuptools, build, wheel
	@venv/bin/python3 -mpip install --quiet --upgrade pip setuptools build wheel
	@echo installing poetry
	@venv/bin/python3 -mpip install --quiet poetry
	poetry install --no-root

clean:
	rm -rf venv

app:
	source venv/bin/activate && venv/bin/python3 setup.py py2app
