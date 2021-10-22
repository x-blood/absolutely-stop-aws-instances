deploy:
	sls deploy

pip_install:
	pip install -r requirements.txt

pip_freeze:
	pip freeze > requirements.txt
