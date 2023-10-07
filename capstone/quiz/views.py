from django.contrib.auth import authenticate, login, logout
from allauth.account.views import SignupView
from allauth.account.forms import SignupForm
from allauth.account.views import LoginView
from django.db import IntegrityError
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import JsonResponse
from .models import Quiz, Question, Choice, UserQuiz, UserResponse, Leaderboard, ProfileImage
import random

# Create your views here.

def index(request):
    return render(request, "quiz/index.html")

def profile_image(request,user_id):
    user = get_object_or_404(User, id=user_id)
    
    if request.method == "POST":
        image = request.FILES.get('profile_image')  # Corrected to use request.FILES
        profile_image, created = ProfileImage.objects.get_or_create(user=user, defaults={'image': image})
        profile_image.image = image  # Update the image if it's changed
        profile_image.save()
        context={
            'user':user,
        }
        return redirect('profile', user_id=user.id)
    return HttpResponse("Profile image updated successfully")
def profile(request,user_id):
    user = get_object_or_404(User, id=user_id)
    profile_image = get_object_or_404(ProfileImage, user=user)
    image = ProfileImage.objects.get(user=request.user)
    
    # save changes
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email_id')
        password = request.POST.get('current_password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            return render(request, 'quiz/profile.html', {'error_message': 'Passwords do not match'})

        if(request.user.id == user_id):
            # Update user information
            if username:
                user.username = username
            else:
                user.username = user.username
            
            if email:
                user.email = email 
            else:
                user.email = user.email                 
           
            if password:  # Check if a new password was provided
                user.set_password(password)

            user.save() # Add this line to confirm if the user information was updated
        else:
            return render(request, 'quiz/profile.html', {'error_message': 'You are not the current user'})

        return redirect('profile', user_id=user.id)

    context = {
        'user': user,
        'profile_image': profile_image,
        'image':image,
    }
    
    return render(request, 'quiz/profile.html', context)

def play(request):    
    error_message = None

    if request.method == "POST":
        code = request.POST.get('code')
        
        try:
            quiz = get_object_or_404(Quiz, id=code)
        
            if code == str(quiz.id): 
                if  quiz.is_closed:
                    error_message = "Quiz Closed!"
                else:
                    return redirect('quiz', quiz_id=code)
            else:
                error_message = "Invalid CODE!"
        except Http404:
            error_message = "Quiz not found."

    return render(request, "quiz/play.html", {'error_message': error_message})

def quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = Question.objects.filter(quiz=quiz)

    questions_and_choices = []

    for question in questions:
        choices = Choice.objects.filter(question=question)
        shuffled_choices = list(choices)
        random.shuffle(shuffled_choices)
        questions_and_choices.append((question, shuffled_choices))
        
    if request.method == 'POST':
        user = request.user
        user_quiz, created = UserQuiz.objects.get_or_create(user=user, quiz=quiz, is_completed=False)
        score = 0
        for question in questions:
            selected_choice_id = request.POST.get(f'question_{question.id}')
            if selected_choice_id:
                selected_choice = get_object_or_404(Choice, id=selected_choice_id)
                UserResponse.objects.create(user_quiz=user_quiz, question=question, choice=selected_choice)
                if selected_choice.is_correct:
                    score += 1
        user_quiz.score = score
        user_quiz.is_completed = True
        user_quiz.save()
        return redirect('leaderboard', quiz_id=quiz.id)
    
    context = {
        'quiz_id': quiz_id,
        'quiz': quiz,
        'questions_and_choices': questions_and_choices,
        'questions_count': questions.count(),
    }

    return render(request, "quiz/quiz.html", context)


def leaderboard(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    user_quiz = UserQuiz.objects.filter(quiz=quiz, is_completed=True).order_by('-score')  # Get completed quizzes, ordered by score
    
    profile_image = []
    for user_q in user_quiz:
        user = user_q.user
        image = ProfileImage.objects.filter(user=user).first()
        profile_image.append((user_q, image.image.url))   
    context = {
        'quiz': quiz,
        'user_quiz_images': profile_image,
    }
    
    return render(request, "quiz/leaderboard.html", context)



def myquiz(request,user_id):
    user = get_object_or_404(User, id=user_id)
    quiz = user.quiz_set.all()
    
    paginator = Paginator(quiz,5)
    page_Number = request.GET.get('page')
    quizes = paginator.get_page(page_Number)
    
    if request.method == "POST":
        quiz_id = request.POST.get('quiz_id')
        
        quiz = get_object_or_404(Quiz, id=quiz_id)
        quiz.is_closed = True
        quiz.save()
        
        return redirect('myquiz', user_id=request.user.id)
    
    context={
        'user':user,
        'quiz' : quizes,
        'quiz_count':quiz.count()
    }
    return render(request,"quiz/myQuiz.html",context)

def createquiz(request):
    if request.method == "POST":
        quiz_title = request.POST.get('quiz_title')
        quiz_description = request.POST.get('quiz_description')
        current_user = request.user
        
        create = Quiz(creator=current_user,title=quiz_title,description=quiz_description,is_published = True)
        create.save()

        # Redirect to the 'question' view with the quiz_id as a parameter
        return redirect('question', quiz_id=create.id)
        
    return render(request, "quiz/createquiz.html")


def question(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    
    if request.method == "POST":
        quiz_questions = request.POST.get('quiz_questions')
        current_user = request.user
        choice_1 = request.POST.get('choice_1')
        choice_2 = request.POST.get('choice_2')
        choice_3 = request.POST.get('choice_3')
        choice_4 = request.POST.get('choice_4')
        correct_answer1 = request.POST.get('correct_answer1')
        correct_answer2 = request.POST.get('correct_answer2')
        correct_answer3 = request.POST.get('correct_answer3')
        correct_answer4 = request.POST.get('correct_answer4')
    
        question = Question(quiz=quiz, text=quiz_questions)
        question.save()
        
        choices_data = [
            {'text': choice_1, 'is_correct': correct_answer1 == '1'},  # Check if the choice corresponds to the correct answer
            {'text': choice_2, 'is_correct': correct_answer2 == '1'},
            {'text': choice_3, 'is_correct': correct_answer3 == '1'},
            {'text': choice_4, 'is_correct': correct_answer4 == '1'},
        ]
        
        for choice_data in choices_data:
            choice = Choice(question=question, **choice_data)
            choice.save()
            
        return redirect('question', quiz_id = quiz.id)
    return render(request, "quiz/question.html", {'quiz': quiz})

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "quiz/login.html", {
                "message": "Invalid username and/or password.",
            })
    else:
        return render(request, "quiz/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)       
        if form.is_valid():
            user = form.save(request)  # Save the user object first
            
            default_image_path = "images/default.jpg"
            profile_image = ProfileImage.objects.create(user=user, image=default_image_path)
            
            # Log in the user
            login(request, user)

            return redirect('index') 
        else:
            return render(request,"quiz/register.html",{'error_message':form.errors})
    else:
        form = SignupForm()
    return render(request, 'quiz/register.html', {'form': form})



    

