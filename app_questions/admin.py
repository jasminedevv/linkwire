from django.contrib import admin
from .models import Article, Question, Score

# Register your models here.
admin.site.register(Article)
admin.site.register(Question)
admin.site.register(Score)