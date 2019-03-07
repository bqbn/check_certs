build: clean
	python setup.py bdist_wheel

clean:
	rm -rf build/
	rm -rf check_certs.egg-info/
	rm -rf dist/

publish: build
	twine upload dist/*

tests:
	python -m unittest check_certs/tests/test_check_certs.py
	python -m unittest check_certs/tests/test_utils.py
