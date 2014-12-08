install:
	python setup.py develop
	python demo/setup.py develop

demo:
	python demo/demo.py

publish:
	python setup.py sdist upload

.PHONY: install demo publish
