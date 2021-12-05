# Web Application (Test)

---


# How To

### Requirements:

To run this codebase, following are needed:
- Python 3.7.0
- pipenv
- .env file with SECRET_KEY(Nevertheless I just added that in this repo this is not best practice
- but for simplicity I did that.)

```
pip3 install pipenv
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
First one might not be needed.
```
pipenv run python manage.py makemigrations --settings=web_service.settings.development  
pipenv run python manage.py migrate --settings=web_service.settings.development
```
This will need gnu gettext (>0.15) please install that before running this. You can also
ignore this command that will only miss the `internationalization` but things will still work.
link https://stackoverflow.com/questions/38806553/how-to-install-gnu-gettext-0-15-on-windows-so-i-can-produce-po-mo-files-in
```
pipenv run python manage.py compilemessages --settings=web_service.settings.development
```

````
pipenv run python manage.py runserver --settings=web_service.settings.development
```

Then you can upload txt file browsing homepage on this address

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
