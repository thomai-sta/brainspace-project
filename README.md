## Installation

You need to have the following installed on your machine:
- Docker
- git
- Python3

### Linux:

Open a terminal and follow the steps below.

Get project from github
```bash
git clone https://github.com/thomai-sta/brainspace-project.git
cd brainspace-project
```

#### Run with docker

Build docker image

```bash
docker build -t dictionary:latest .
```

Run docker container
```bash
docker run -d -p 8080:8080 dictionary
```

Open a browser and go to ```0.0.0.0:8080```. Application should be up and running.

To stop the container:
```bash
docker container ls
```
Find the container for the dictionary image and copy its name
```bash
docker stop <containers_name>
```

#### Run manually

If the docker approach does not work, you can setup and run the application manually. First., create and activate a virtual environment:
```bash
python3 -m venv venv
. venv/bin/activate
```

```bash
pip install dist/dictionary-1.0.0-py3-none-any.whl
```

```bash
export FLASK_APP=dictionary
flask init-db
pip install waitress
waitress-serve --call 'dictionary:create_app'
```

Open a browser and go to ```0.0.0.0:8080```. Application should be up and running.

### Windows

Open a cmd prompt and follow the steps below.

Get project from github
```bash
git clone https://github.com/thomai-sta/brainspace-project.git
cd brainspace-project-main
```

#### Run with docker

Build docker image

```bash
docker build -t dictionary:latest .
```

Run docker container
```bash
docker run -d -p 8080:8080 dictionary
```

Open a browser and go to ```localhost:8080```. Application should be up and running.

To stop the container:
```bash
docker container ls
```
Find the container for the dictionary image and copy its name
```bash
docker stop <containers_name>
```

*In Windows once you build the image, you can stop and start the container from the interface of Docker Desktop.*
#### Run manually

If the docker approach does not work, you can setup and run the application manually. First., create and activate a virtual environment:
```bash
python3 -m venv venv
cd venv/Scripts/
activate.bat
cd ../../
```

```bash
pip install dist/dictionary-1.0.0-py3-none-any.whl
```

```bash
set FLASK_APP=dictionary
flask init-db
pip install waitress
waitress-serve --call "dictionary:create_app"
```

Open a browser and go to ```localhost:8080```. Application should be up and running.

**With this method, there is an issue with the DB initialization (it does not initialize), so index page is running, but no request can be handled.**


## Description

This is a basic dictionary application. It maintains a local database of words and if a searched word is not found locally, it connects to https://dictionaryapi.dev/ to retrieve the information. The information is then automatically saved locally, so if the same word is searched again, it will be retrieved from the local DB. Only the various definitions of the words are displayed, even though all the retrieved information is stored locally. There is also a register/login/logout functionality, however at the moment it is of no use to the application.

Next steps could be:

- Word is saved locally only by registered users
- Locally saved words are associated to the user and each user can see a list of their saved words (also delete words)
- More information of the words can be displayed
- List of locally saved words should be grouped and displayed in pages, so that table does not get extra long
- An alphabetized selection should be possible, so that the user can see words based on their initial
- Ordering of the table should be adjustable (currently alphabetically based on word)



Some screenshots of the application can be found in the corresponding folder of the repo!
