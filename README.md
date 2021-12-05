# Web Application (Test)

---


# How To

### Requirements:

To run this codebase, following are needed:
- Python 3.7
- pipenv


### Preparation

First clone the repository using
```
$ git clone https://github.com/shaifulislamboby/web_service.git
```
Then setup Virtual Environment.

## Once pipenv is installed you can execute the following command
`pipenv sync`  This will install all the required package and
 also create a virtual environment if needed.

### Starting

Finally, to start the project run this commands in sequence
```
pipenv run python manage.py makemigrations --settings=web_service.settings.development
pipenv run python manage.py migrate --settings=web_service.settings.development
pipenv run python manage.py compilemessages --settings=web_service.settings.development
pipenv run python manage.py runserver --settings=web_service.settings.development
```


### Testing
Need to write unittests according to the requirements.

---

### Todos:

- [ ] add tests
- [ ] refactor/ for adding new separators list can be added, 
- [ ] Error handling can be improved 
- [ ] Airflow can be used for orchestrating
- [ ] organize things properly
- [ ] add more comprehensive comments
- [ ] file naming and locations can be changed in main function
