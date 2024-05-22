from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("profile/<int:user_id>/", views.profile, name="profile"),
    path("profile_image/<int:user_id>/", views.profile_image, name="profile_image"),
    path("myquiz/<int:user_id>/",views.myquiz,name="myquiz"),
    path("create_quiz/",views.createquiz,name="create_quiz"),
    path("create_quiz/questions/<int:quiz_id>/",views.question,name="question"),
    path("play/",views.play,name="play"),
    path("play/quiz/<int:quiz_id>/",views.quiz,name="quiz"),
    path("play/quiz/leaderboard/<int:quiz_id>/",views.leaderboard,name="leaderboard"),
]