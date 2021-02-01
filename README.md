# Project 1 - Continuous Integration Test

### How to run - development
1. clone and cd into repo
2. `$ python -m venv env`
3. `$ source env/bin/activate`
4. `$ pip install -r requirements.txt`
5. `export FLASK_ENV=development`
6. `export FLASK_APP=converter`
7. `export WOLFRAM_APP_ID={wolfram api app id, required}`
8. to run the app locally: `$ flask run`
9. to run tests (with coverage): `$ python -m coverage run -m pytest`
10. to view covereage report: `$ coverage report -m`
