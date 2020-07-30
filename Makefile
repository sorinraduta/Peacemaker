VENV=.venv
PYTHON_BIN=python3

start: venv
	${PYTHON_BIN} bot.py

requirements: requirements.txt

venv: requirements
	test -d $(VENV) || $(PYTHON_BIN) -m venv $(VENV)

test: requirements.txt
	$@
