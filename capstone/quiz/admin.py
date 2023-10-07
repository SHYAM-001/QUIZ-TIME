from django.contrib import admin
from .models import Quiz, Question, Choice, UserQuiz, UserResponse, Leaderboard, ProfileImage

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(UserQuiz)
admin.site.register(UserResponse)
admin.site.register(Leaderboard)
admin.site.register(ProfileImage)
