
# Hi, I'm Shyam K S! 👋


# Quiz Time

QuizMaster is a dynamic web application built on Django, designed to provide users with an engaging quiz-taking experience. Whether you're a trivia enthusiast or looking to test your knowledge in a specific domain, QuizMaster has something for everyone.




## Installation

Install my-project with `git clone `

##### Get started!

```bash
   create a folder in the name you needed `your folder name`
```
```bash
  git clone https:
```
    
## Environment Variables

To run this project, you will need to run the virtual Environment file `myVenv`

```bash
   source myVenv/Scripts/activate
```
If your system doesn't have the virtual Environment then,

```bash
   pip install venv
```


## To Run the project

### After cloning and running `myVenv` 
To run the `myVenv`
```bash
source myVenv/Scripts/activate
```

Install django in the virtual environment

```bash
  pip install django
```
To add profile image in the project,first install `pillow`

```bash
  pip install pillow
```

start the database to run

```bash
   python manage.py makemigrations
```
```bash
   python manage.py migrate
```

After migration to manage the database create a superuser

```bash
   python manage.py createsuperuser
```

Go to the project directory

```bash
  cd capstone
```

Start the server

```bash
  python manage.py runserver
```

# Setting the Settings.py file for saving the `Profile Image`
Setting the static file 
```bash
STATIC_URL = 'static/'
```

### Base directory for media files

```bash
MEDIA_URL = '/images/'
```
```bash
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```
```bash
MEDIA_ROOT = os.path.join(BASE_DIR, 'static')
```

## Authors

- [@SHYAM-001](https://www.github.com/SHYAM-001)

