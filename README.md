# Storefront Tutorial: 
- Following this tutorial: https://codewithmosh.com/p/the-ultimate-django-series

# Project Set Up
- Create directory
- `cd` into directory and `pip3 install pipenv`
  - pipenv: dependency management tool to install app deps in a virtual env
- Install Django with pipenv inside a virtual env: `pipenv install django`
  - This creates a directory in your virtualenvs folder
  - Creates two files: PipFile and Pipfile.lock
- Create a project in the current directory using django-admin: `django-admin startproject storefront .`
  - This adds the `storefront` app folder and the `manage.py` file (wrapper around djang-admin). Can use `manage.py` now instead of django-admin.
  - At this point, if we `runserver` with django-admin, we will get an error. 
  - Runserver with manage.py: `python manage.py runserver`
    - Default port is 8000
    - Specify port number command: `python manage.py runserver.py <port-number>`
  - View available commands with: `python manage.py`

- *Possible Error*: Need to activate virtual env
  - If you see the following error, need to activate the virtualenv.
  ```
   File "manage.py", line 17
    ) from exc
         ^
  ```
- Active virtual environment: `pipenv shell`
- Exit virtual environment: `control^ + D` 

## VSCode and Python
- Setup steps so VSCode integrated terminal starts virtual environment on open (`control^ + backtick`)
- Open `Command Pallette` and search for `Python Interpreter`
- Python Interpreter is default set to the globally installed python interpreter. Need to select the python interpreter in the virtual environment (for this project). Enter the path here. `Current: ~/path/to/python/interpreter/in/virtual/env`
- Find virtualenv python interpreter path: In terminal run -- `pipenv --venv`
  - This returns: `path/to/virtualenvs/project-virtualenv`
  - When adding it to VSCode, need to add `.../bin/python` to the end of the path. Example: `path/to/virtualenvs/project-virtualenv/bin/python`
