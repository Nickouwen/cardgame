# cardgame
A simple card game based off a French card game

## How to contribute to development
1. Clone repository to new directory
2. Create a python virtual environment
3. Within the virtual environment, install the required dependencies
4. Run from a django server or from console_main

### Clone Repository to new directory
<code>> git clone -b 'branch' 'repository' 'empty-target'</code>

### Create a python virtual environment
<code>> python -m venv path/to/virtual/environment</code>

### Within the virtual environment, install the required dependencies
1. Activate the virtual environment
   - From git CLI:
```$ source path/to/virtual/environment/Scripts/activate```
   - From command line:
```> path\to\virtual\environment\Scripts\activate.bat```
2. Install the required dependencies
<code>> pip install -r requirements_dev.txt</code>

### Run Django server or from console_main
```
"configurations": [
        {
            "name": "Python: Django",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/dev/src/manage.py",
            "args": [
                "runserver"
            ],
            "django": true,
            "justMyCode": true
        },
        {
            "name": "cardgame_test",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/dev/src/console_main.py",
            "console": "integratedTerminal",
            "justMyCode": true
        }
    ]
```

# Style Guide
https://phalt.github.io/django-api-domains/
