build: clean
	python setup.py bdist_wheel

clean:
	rm -rf build/ dist/

publish:
	twine upload dist/*
