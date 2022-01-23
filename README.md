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
- View installed packages: `pip list`
- Install all dependencies in virtual environment: `pipenv install`

## VSCode and Python
- Setup steps so VSCode integrated terminal starts virtual environment on open (`control^ + backtick`)
- Open `Command Pallette` and search for `Python Interpreter`
- Python Interpreter is default set to the globally installed python interpreter. Need to select the python interpreter in the virtual environment (for this project). Enter the path here. `Current: ~/path/to/python/interpreter/in/virtual/env`
- Find virtualenv python interpreter path: In terminal run -- `pipenv --venv`
  - This returns: `path/to/virtualenvs/project-virtualenv`
  - When adding it to VSCode, need to add `.../bin/python` to the end of the path. Example: `path/to/virtualenvs/project-virtualenv/bin/python`

# Creating a New App
- `python manage.py startapp <new-app-name>`
- This will create a new directory called `playground` at the same level as `storefront` app, at the base of the file tree.
- *Register new app* in projects `settings.py` module: 
  - In the storefront project folder: go to `settings.py`: 
  - `INSTALLED_APPS`: After the list of Django's apps, add the newly created app (`storefront`). 

## Django App Structure
- `migrations` folder: used for generating database tables
- `admin.py` module: admin interface
- `apps.py` module: for defining the app
- `models.py` module: used for building model classes for the app that are used for getting data for the user
- `tests.py` module: unit tests
- `views.py` module: controllers/business logic. Request handler. 

# URLs - Views - Templates
## URLConf
- one main `urls.py` where urls matching a certain pattern can be routed to a specific apps `urls.py` module.
- urls convention END with a `/`. Ex: `playground/hello/`

## Views --> Django Templates
- Django Template Engine: Default template engine can be replaced with a template engine of your choice.
- View function can return a template (.html).
- Django template can be passed variables from the views function as a dictionary object (3rd argument in the `render` function)
- Views `render` function takes 3 parameters: `request`, `template name as a string`, `variables to pass to the template`.
- Templates use the passed variables by surrounding the variable in double curlies: ex. `{{ variable_key_from_dictionary }}`
- Templates can conditionally render parts of the template using `if` and `if/else` statements. 
  ```
  {% comment %}
  <!-- Example Comment: -->
  <!-- This comment will not be rendered -->
  <!-- More on Django templates: https://docs.djangoproject.com/en/4.0/topics/templates/ -->
  {% endcomment %}

  {% if abc %}
  <p>Do this</p>
  {% else %}
  <p>Otherwise do this</p>
  {% endif %}
  ```

# Debugging in VSCode
## Setup VSCode Debugger (first time setup for a project)
- Open `Run and Debug` by clicking the bug with the play triangle (or `command + shift + D`).
  - Note: the first time this is opened, you will be prompted to create a `launch.json` file. This file lives in the `.vscode` folder. Select `python` --> `django`. This will auto generate a launch.json file that will be used to tell VSCode how to run debugger.
- `launch.json` args (port overlap): debugger default runs on port 8000 which is being used by storefront project. Can pass a port number (as a string) as a second item in list under `args` in launch.json to specify a different port. 
## Start Debugger
- Add red vscode breakpoint by clicking left of the line number.
- Click green button in `run and debug` to start debugger. It will continue until it hits a red vscode breakpoint. 
  - *Possible Error*: If you see an `ImportError`, could possibility be a VSCode interpreter issue. Try setting up the python interpreter again. Resource: https://oraclefrontovik.com/2021/08/19/exception-has-occurred-importerror-couldnt-import-django-when-debugging-django-with-vs-code/
- Debug server should start on specified port. Open Chrome/browser and go to local host at that port, and hit the endpoint that has the debugger
- `Run and Debug` Sections: 4 dropdowns
  - Can see Local variables in the 1st dropdown
  - Can add/view variables to watch in the 2nd dropdown
  - Can view call stack in 3rd dropdown
  - Can view/add/remove breakpoints in 4th dropdown
- Debugger Options:
  - Continue: continue all the way through or until next debugger
  - Step Over: step over entire function
  - Step Into: execute line by line
  - Stop Over: exit the current function the breakpoint is in
  - Restart: restart debugger (need to refresh page/hit the endpoint the debugger is in again)
  - Stop/Disconnect from debugger
- Note: Remove breakpoints once done

## VSCode Run App Shortcuts:
- Run WITHOUT Debugger: `control + F5`
- Run WITH Debugger: `F5`
- Note: This can also be found in VSCode top menu bar under `Run`.

## Django Debug Toolbar
- Docs: https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
- Install Django Debug Toolbar & Setup: 
  - We want to install it in the project's virtual environment. To do so, activate virtual environment: open vscode integrated terminal OR enter `pipenv shell` in terminal
  - Install in Virtual Environment: `python -m pip install django-debug-toolbar` or `pipenv install django-debug-toolbar`
  - Check installation list: `pip list`
  - Add `debug_toolbar` (for django-debug-toolbar) to list of `INSTALLED_APPS` in project apps. This is under `settings.py` module in project folder.
  - Add new url pattern in the project's main URLConf module -- `path('__debug__/', include('debug_toolbar.urls')),`
  - Add to `MIDDLEWARE` in `settings.py` module: goes between django's `request/response` cycle. 
  - Add IP Address to `INTERNAL_IPS` list if it exists in `settings.py` module. This does not exist by default in a new django project. If it does not exist, add the entire list with the internal IP. This can go anywhere in the `settings.py` file.
- Start Django Debug Toolbar:
  - Go page in the browser
  - Note: django debug toolbar will only appear if the page returns a *proper* html document. Needs at least `<html><body> template logic </html></body>`
- Django Debug Toolbar will appear on the right in the browser:
  - Tool bar sections
    - History, versions, time, settings, headers, etc.
    - Note: SQL Panel: Can view queries sent to the database from Django here.
