# Web Application (Test)

---


# How To

### Requirements:

To run this codebase, following are needed:
- Python 3.7
- pipenv

```
pip install pipenv
```


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

Then u can upload txt file browsing

```
http://localhost:8000/
```

That will save the data and parse the file if possible to another model with 
detail information. If you uploaded a valid txt file and the system has parsed it then 
you can access the endpoints for the info.

```
    http://localhost:8000/one-random-line/
    http://localhost:8000/one-random-line-backwards/
    http://localhost:8000/hundreds-longest-lines/
    http://localhost:8000/twenty-longest-lines/
```
You can use postman or other services as per your preference.

### Testing
For running tests please run 
```
pipenv run python  manage.py test  api_services.tests --settings=web_service.settings.development
```

---

### Todos:

- [ ] add tests, more test can be added
- [ ] refactor/ for few function can be made, 
- [ ] Error handling can be improved
- [ ] organize things properly
- [ ] add more comprehensive comments
- [ ] some function may be named poorly, that can be improved 
