run:
	FLASK_APP=flaskr FLASK_ENV=development flask run
run-80:
	FLASK_APP=flaskr FLASK_ENV=development FLASK_RUN_PORT=80 flask run
init-db:
	export FLASK_APP=flaskr export FLASK_ENV=development flask init-db
