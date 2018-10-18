from django.db import models

# TODO: add image support 
class Article(models.Model):
    title = models.TextField()
    link = models.TextField()
    def __str__(self):
        return self.title

class Question(models.Model):
    title = models.TextField()
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    def __str__(self):
        return (self.title)

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     score = models.IntegerField(default=0):10345