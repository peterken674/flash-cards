# FLASH CARD
Author:[Nancy Kemunto](https://github.com/nancy88199488)
Author:[Peter Kennedy](https://github.com/peterken674)
Author:[Gabriel Ayuel](https://github.com/ayuelgarang105)  
  
# Description  

This is a tiny flash cards where you can write anything you think seems important in order to keep them safe.

## User Story  
As a user, I would like to:

* A user must be authenticated to see his flashcards.
* A user's flash card can contain a title with some notes.
* Flashcards should be organized according to subjects/courses.
* A user can delete or update a flash card he has created.
* A user should see when the flash card was created and when it was last updated.
 

  
## Setup and installations
* Fork the data .
* git clone the gallery repo.
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3 manage.py runserver`



## Getting started

### Prerequisites
* python3.6
* virtual environment
* pip

#### Clone the Repo 
```bash
git clone (link here)
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment
```bash
python3 -m venv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY='**'
DEBUG=True
DB_NAME='****'
DB_USER='<your database name>'
DB_PASSWORD='<password to your database>'
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
DISABLE_COLLECTSTATIC=1
```

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3 manage.py check
python manage.py makemigrations gallery
python3 manage.py sqlmigrate gallery 0001
python3 manage.py migrate
```

#### Run the app
```bash
python3 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)



## Testing the Application
`python manage.py test instaClone`
        
## Technologies Used

* [Python3.8](https://docs.python.org/3/)
* Django 
* Postgresql 
* Boostrap
* HTML

## Contact Information   
Please, contact any of the authors above for any question or contributions
  
## License 

[MIT](LICENSE.md) <br>
Copyright © by Nancy, Peter and Gabriel. 
