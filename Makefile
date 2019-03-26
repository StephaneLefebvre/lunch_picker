JOB_NAME = lunch_picker
WORKSPACE = .

mkvirtualenv:
	virtualenv --system-site-packages -p python3 $(JOB_NAME)

install: mkvirtualenv 
	${WORKSPACE}/$(JOB_NAME)/bin/pip install --upgrade pip
	${WORKSPACE}/$(JOB_NAME)/bin/pip install -r requirements.pip

review: mkvirtualenv
	${WORKSPACE}/$(JOB_NAME)/bin/pip install pylint
	${WORKSPACE}/$(JOB_NAME)/bin/pylint --version
	${WORKSPACE}/$(JOB_NAME)/bin/pylint -f parseable --max-line-length=80 *.py

microservice: install
	${WORKSPACE}/$(JOB_NAME)/bin/python src/lunch_picker_microservice.py &
	echo "yes"

server: install
	${WORKSPACE}/$(JOB_NAME)/bin/python src/server.py &
	echo "yes"

all: microservice server
	echo "yes"
