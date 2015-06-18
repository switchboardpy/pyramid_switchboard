VERSION = $(shell python setup.py --version)

install:
	python setup.py develop
	python demo/setup.py develop

demo:
	python demo/demo.py

release:
	git tag $(VERSION)
	git push origin $(VERSION)
	git push origin master
	python setup.py sdist bdist_wheel
	twine upload dist/pyramid_switchboard-$(VERSION)*

.PHONY: install demo release
