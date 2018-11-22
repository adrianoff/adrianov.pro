adrianov.pro webpage

How to create virtual env: 

	virtualenv -p /usr/bin/python3 venv/
	
	source env/bin/activate
	
	pip install -r requirements.txt

To start uwsgi use command: 
	
	uwsgi --ini ./src/src/uwsgi.ini
