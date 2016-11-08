# App Engine Python Backend Seed
A seed for a python backend using Flask on App Engine.

## Setup

- Install Google App Engine Launcher;
- Install pip & virtualenv;
- Run `./bin/init.sh` to initiate an isolated python environment;
- Run `source venv/bin/activate` to activate the isolated python environment.

## Unit tests

Run `nosetests` in the root directory.

## App Engine

App Engine has no dependency management system and requires the dependencies to be included.
The seed uses linkenv to go around this limitation.
Run `linkenv venv/lib/python2.7/site-packages libs` after adding new dependencies to remain compliant.

## Install new dependencies

- Make sure your isolated environment is activated;
- Run `pip install <dependencies>`;
- Run `linkenv venv/lib/python2.7/site-packages libs`;
- Add the dependencies in the proper requirements file.

## Scripts

- init: initialises environment (virtualenv + development dependencies)
- dev: sets environment (dependencies) to development
- deploy: installs production dependencies and deploys to App Engine
- run: runs the application in App Engine mode