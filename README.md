## Installation

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