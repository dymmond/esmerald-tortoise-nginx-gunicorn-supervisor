# {{ cookiecutter.project_name }}

This platform runs on the top of [Esmerald](https://esmerald.dymmond.com).

---

## Table of Contents

- [{{ cookiecutter.project_name }}](#-cookiecutterproject_name-)
    - [Table of Contents](#table-of-contents)
    - [Introduction](#introduction)
    - [Requirements](#requirements)
    - [Instalation](#instalation)
    - [Deployment](#deployment)
    - [Endpoints](#endpoints)
    - [OpenAPI](#openapi)
    - [Disclaimer](#disclaimer)

---

## Introduction

This cookiecutter served by Esmerald serves the purpose of a scaffold example for an application
using:

* [Esmerald](https://esmerald.dymmond.com)
* [Tortoise ORM](https://tortoise.github.io/)
* [Nginx](https://www.nginx.com/)
* [Gunicorn](https://gunicorn.org/)
* [Supervisor](http://supervisord.org/)
* [Uvicorn](https://www.uvicorn.org/)

Brings also an initial migration using [Esmerald supported](https://esmerald.dymmond.com/databases/tortoise/models/)
tables.

## Requirements

1. Python 3.8+.
2. [Esmerald](https://esmerald.dymmond.com).
3. Virtual environment.
4. Docker
5. [Aerich](https://github.com/tortoise/aerich)

## Instalation

After creating a virtual environment at your choice.

1. `make requirements` - Installs the requirements to run the development environment.
2. `docker compose up` - Starts the docker compose for databases and redis.
3. `make upgrade` - Runs the migrations against the database.
4. `make test` - Runs the local tests.
5. `make run` - Starts the development environment with the development settings.

You can now access the `http://localhost:8000`

```shell
INFO:     Uvicorn running on http://localhost:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28061] using WatchFiles
INFO:     Started server process [28063]
INFO:     Waiting for application startup.
```

## Deployment

Every project has its own strategy but this cookiecutter brings a `deployment` folder containing
all the files needed and prepared for the nginx, supervisor and gunicorn used for a deployment
as well as a `Dockerfile` prepared to be built.

## Endpoints

* [Health check](http://localhost:8000/health-check) - http://localhost:8000/health-check
* [Welcome](http://localhost:8000/api/v1/welcome) - http://localhost:8000/api/v1/welcome

## OpenAPI

You can access the application docs via:

* http://localhost:8000/docs/swagger
* http://localhost:8000/docs/redoc

## Disclaimer

This is not mandatory to be used and serves as quick entry point for applications that need to be
deployed in a production environment and helps speeding up the process. Feel free to discard what is
not needed.