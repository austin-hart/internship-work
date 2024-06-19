VENV := env

../$(VENV)/bin/activate: requirements.txt
	cd .. && python3 -m venv $(VENV)
	../$(VENV)/bin/pip install -r requirements.txt

# venv is a shortcut target
venv: ../$(VENV)/bin/activate

path:
    export PYTHONPATH=$(pwd):$(pwd)./project/grpcdocs

test: venv path
	../$(VENV)/bin/python3 -m unittest discover ./tests

run-client: venv path 
	../$(VENV)/bin/python3 ./project/grpcdocs/client.py

run: venv path
	../$(VENV)/bin/python3 ./project/app.py

run-client-test: venv path
	../$(VENV)/bin/python3 ./project/service/test_client.py

run-mint: venv path
	../$(VENV)/bin/python3 ./tests/mint_USDC.py

lint: venv path
	../env/bin/python3 -m pylint --ignore-paths=./project/grpcdocs/* ./project/

type-check: venv path
	../env/bin/python3 -m mypy ./service/

clean:
	rm -rf ../$(VENV)
	find . -type f -name '*.pyc' -delete