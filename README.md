<p align=center>
  <img src="https://www.django-rest-framework.org/img/logo.png" alt="django-rest-logo" height=200>
</p>

# Task Manager

## Description

An in memory (NO DATABASE) web application CRUD based RESTful backend for managing personal tasks and notes within a given task.

<p align=center>
  <img src="https://i.ibb.co/BqZ1fnN/task-manager-djangorest-console.gif" alt="sample-run-gif" height=auto>
</p>

### Pre-setup dependencies

- Git
- Python3

### Setup

`HTTPS`

```bash
git clone https://github.com/Ak-Shaw/task-manager-djangorest.git
```

`SSH`

```bash
git clone git@github.com:Ak-Shaw/task-manager-djangorest.git
```

`dependencies`

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python3 manage.py migrate --run-syncdb
```

### Usage

`run server`

```bash
source env/bin/activate
python3 manage.py runserver
```

`testing`

```bash
python3 manage.py test
```

Refer API Usage [here](rest.http).
