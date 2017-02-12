clean:
	rm -rf build dist littleblog.egg*
build: clean
	python setup.py sdist bdist_wheel
upload:
	twine upload dist/*
	clean
