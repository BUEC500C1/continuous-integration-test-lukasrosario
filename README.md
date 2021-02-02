# Project 1 - Continuous Integration Test

### How to run - development

1. clone and cd into repo
2. `$ python -m venv env`
3. `$ source env/bin/activate`
4. `$ pip install -r requirements-dev.txt`
5. `$ export FLASK_ENV=development`
6. `$ export FLASK_APP=converter`
7. `$ export WOLFRAM_APP_ID={wolfram api app id, required}`
8. to run the app locally: `$ flask run`
9. to run tests (with coverage): `$ python -m coverage run -m pytest`
10. to view covereage report: `$ coverage report -m`

#### You can check out the app at https://ec500-ci-test.herokuapp.com/ as well (using free tier so it might take a minute to spin up)

### Notes

- Firstly, my implementation takes a pretty naive approach to parsing the user input. I attempted to address certain peculiarities in my tests, but there are absolutely more cases that could be tested for and corrected automatically (I use the Wolfram Short Answers API, but of course it's not perfect and needs help sometimes).
- Deciding to have a UI in the form of a web app presented some interesting challenges. Most notably, writing tests becomes a more involved process. Here, again, I chose a more naive approach (for simplicity's sake). Specifically, I expose the app's endpoint to accept user input via an HTML form or JSON. When writing tests, I send POST requests with JSON using the python requests library. However, this is ultimately not representative of the actual user experience, as users would submit a question using the form, not with code.
- More on the above point, there are ways to test HTML functionalities with pytest, but I was not able to make enough time to try to implement them.
- When testing for the accuracy of converted values, I use a bit of an arbitrary criteria that checks if the value returned from the Wolfram API is within 0.5% of the value I get when I Google the same question. Context matters and while I don't really have an issue with it for this assignment it probably isn't something NASA would want to use.
- Final point, I tried to connect my Heroku app to this repo so I could add a workflow for automatic deployments of the main branch, but I wasn't able to because the repo is under a classroom and Heroku needs permission. It was a bit too late for me to ask about it over email for this assignment, but would you be willing to approve these connections to the classroom so we can implement them in later projects?
