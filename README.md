# Hi, I'm Shyam K S! 👋


# Quiz Time

QuizMaster is a dynamic web application built on Django, designed to provide users with an engaging quiz-taking experience. Whether you're a trivia enthusiast or looking to test your knowledge in a specific domain, QuizMaster has something for everyone.

# Key Features:
- User Authentication: Create a personalized account to track your quiz progress and scores.

- Quiz Categories: Choose from a diverse range of categories spanning sports, science, pop culture, and more.

- Leaderboard: Compete with other users and see where you stand in the global rankings.

- Profile Customization: Personalize your profile with a unique avatar and background image.

- Interactive UI: Intuitive and user-friendly interface for seamless quiz navigation.

- Responsive Design: Enjoy the same great experience on both desktop and mobile devices.


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

# Open Your Browser:
Visit http://localhost:8000 to start exploring the QuizMaster!

# Contributing:
We welcome contributions from the community! If you have ideas for new features, improvements, or find any bugs, please open an issue or submit a pull request.

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

