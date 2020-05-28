
install:
	pip install -r calculon/requirements/common.txt

run:
	python manage.py runserver 0.0.0.0:3000

replit_refresher:
	make install
	make run
