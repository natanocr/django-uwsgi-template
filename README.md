# <!-- {% comment %} -->Django uWSGI template
<!-- {% endcomment %}--> {{project_name}}

This is a [Django](https://docs.djangoproject.com) project <!-- {% comment %} -->template<!-- {% endcomment %}--> using [uWSGI](https://uwsgi-docs.readthedocs.io) as application server.

> **NOTE**: for OSX check [uwsgi-emperor-mode](https://github.com/20tab/uwsgi-emperor-mode) to configure your own local server with emperor.

## Documentation

* [Conventions](#conventions)
* [Workspace initialization](#workspace-initialization)
    * [Virtual environment](#virtual-environment)
    * [Basic requirements](#basic-requirements)
<!-- {% comment %} -->
* [Setup a new project](#setup-a-new-project)
    * [Start Project](#start-project)
    * [Git initialization](#git-initialization)
    * [Initialization](#first-initialization)
<!-- {% endcomment %} -->
* [Clone and start the existing project](#clone-and-start-the-existing-project)
    * [Clone Project](#clone-project)
    * [Initialization](#initialization)
* [Usage](#usage)
    * [Database reset](#database-reset)
    * [Superuser creation](#superuser-creation)
    * [Add or Update libraries](#add-or-update-libraries)
        * [List outdated libraries](#list-outdated-libraries)
        * [Edit and Compile requirements files](#edit-and-compile-requirements-files)
    * [Install libraries](#install-libraries)
* [Testing](#testing)
* [Frontend build](#frontend-build)
* [Continuous Integration](#continuous-integration)
* [Deploy](#deploy)

## Conventions

- replace `projects` with your actual projects directory
<!-- {% comment %} -->
- replace `project_name` with your chosen project name

- replace `git_repository_url` with your actual git repository url
<!-- {% endcomment %} -->
## Workspace initialization

We suggest updating pip to the latest version and using a virtual environment to wrap all your libraries.

### Virtual environment

**IMPORTANT**: Please, create an empty virtual environment, with the right python version, and activate it.
To install and use virtualenv, please, visit [the official documentation](https://virtualenv.pypa.io)

### Basic requirements

**Django** and **Invoke** must be installed before initializing the project.

```shell
({{project_name}}) $ pip install -U django invoke
```

<!-- {% comment %} -->
## Setup a new project

This section explains the first steps when you need to create a new project.

### Start Project

Change directory and start a new project with this template:

```shell
({{project_name}}) $ cd ~/projects/
({{project_name}}) $ django-admin.py startproject --template https://www.20tab.com/template/ -e cfg,ini,json,md,py,yaml,template -n Makefile {{project_name}}
```

### Git initialization

In order to initialize git and sync the project with an existing repository:

```shell
({{project_name}}) $ cd ~/projects/{{project_name}}
({{project_name}}) $ inv gitinit GIT_REPOSITORY_URL
```

### First initialization

Go to the [initialization](#initialization) section
<!-- {% endcomment %} -->

## Clone and start the existing project

This section explains the steps when you need to clone an existing project.

### Clone Project

Change directory and clone the project repository:

```shell
({{project_name}}) $ cd ~/projects/
({{project_name}}) $ git clone GIT_REPOSITORY_URL {{project_name}}
```

> **NOTE** : If you're cloning an existing project, make sure you go to the correct branch (e.g. `git checkout develop`)

### Initialization

Enter the newly created **project** directory:

```shell
({{project_name}}) $ cd ~/projects/{{project_name}}
```

Invoke init and follow instructions, to configure the project:

```shell
({{project_name}}) $ inv init
```

## Usage

### Database reset

To reset database execute (beware all data will be lost):

```shell
({{project_name}}) $ inv dropdb
({{project_name}}) $ inv createdb
({{project_name}}) $ python manage.py migrate
```

### Superuser creation

Create a user with full privileges (e.g. admin access):

```shell
({{project_name}}) $ python manage.py createsuperuser
```

### Add or Update libraries

#### List outdated libraries

To list all outdated installed libraries:

```shell
({{project_name}}) $ pip list -o
```

#### Edit and Compile requirements files

Edit the appropriate .ini requirements file, to add/remove pinned libraries or modify their versions.

To update the compiled requirements files (`requirements/*.txt`), execute:

```shell
({{project_name}}) $ make pip
```

Alternatively, in order to update specific dependent libraries to the latest version (e.g. urllib3), execute:
￼
```shell
({{project_name}}) $ make pip p='-P urllib3'
```

### Install libraries for development

To install the just updated requirements (e.g. `requirements/dev.txt`), execute:

```shell
({{project_name}}) $ make dev
```

## Testing

To run the full test suite (including `behave` tests), with coverage calculation, execute:

```shell
({{project_name}}) $ make test
```

> **NOTE**:  check [django-bdd-toolkit](https://github.com/20tab/django-bdd-toolkit) for instructions on how to write BDD tests

## Frontend build

In order to install `node` dependencies and compile the frontend code, execute:

```shell
({{project_name}}) $ make npm
```

## Continuous Integration

Use the following command as a shortcut to configure a continuous integration (e.g. Jenkins) build:

```shell
make ci PASSWORD=<database_user_password> DATABASE=<database_name> SECRETKEY=<django_secret_key>
```

## Deploy

The project is partially configured to use Ansible to deploy the project. For each instance to deploy (e.g. "alpha"), there must be a config file (e.g. `deploy/alpha.yaml`) and an item in the hosts file.

Use provided `deploy/alpha.yaml.template` and `deploy/hosts.template` as templates for, respectively, the configuration and the hosts files. Rename them removing the `.template` suffix. The obtained files will not be versioned.

This project contains makefile commands for "alpha". If needed, duplicate those and use them as templates for additional instances (e.g. "beta" or "prod").

Both the remote server and the continuous integration system need `node.js`, in order to automatically build static files. If such module bundler is not necessary, remove unused commands from the Makefile `ci` command and from `deploy/deploy.yaml`.

Each instance (e.g. "alpha") should be initialized, executing only **once**:

```shell
({{project_name}}) $ make initalpha
```

To deploy a specific instance (e.g. "alpha"), execute:

```shell
({{project_name}}) $ make alpha
```
