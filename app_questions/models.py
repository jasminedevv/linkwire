from django.db import models
from django.contrib.auth.models import User

# TODO: add image support 
class Article(models.Model):
    title = models.TextField()
    link = models.TextField()
    date_displayed = models.DateField()
    def __str__(self):
        return self.title

class Question(models.Model):
    title = models.TextField()
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    answer = models.IntegerField()
    def __str__(self):
        return (self.title)

class Score(models.Model):
    total_right = models.IntegerField(default=0)
    total_wrong = models.IntegerField(default=0)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

# class CustomUser(AbstractUser):
#     score = models.ForeignKey(Score, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.username