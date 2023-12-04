# azurefunc_pythonv2
## Demo of python v2 programming model using blueprints
```
<project_root>/
 | - .dockerignore/
 | - .vscode/
 | - function_app.py
 | - Functest1/
 | | - main.py
 | - Functest2/
 | | - main.py
 | - .funcignore
 | - .gitignore
 | - host.json
 | - requirements.txt
 | - Dockerfile
```
The main project folder, <project_root>, can contain the following files:

* `.venv/`: (Optional) Contains a Python virtual environment that's used by local development.
* `.vscode/`: (Optional) Contains the stored Visual Studio Code configuration. To learn more, see Visual Studio Code settings.
* `function_app.py`: The default location for all functions and their related triggers and bindings.
* `Functest1/`: Contains the `main.py` for our first function.
* `Functest2/`: Contains the `main.py` for our second function.
* `.funcignore`: (Optional) Declares files that shouldn't get published to Azure. Usually, this file contains `.vscode/ `to ignore your editor setting, `.venv/` to ignore local Python virtual environment, and `local.settings.json` to prevent local app settings being published.
* `host.json`: Contains configuration options that affect all functions in a function app instance. This file does get published to Azure. Not all options are supported when running locally.
* `requirements.txt`: Contains the list of Python packages the system installs when it publishes to Azure.
* `Dockerfile`: (Optional) Required only when publishing your project in a custom container.
