from django.db import models
from django.utils import timezone

# Create your models here.

class Conference(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class Division(models.Model):
    name = models.CharField(max_length=10)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=40)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, null = True)
    wins = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    defeats = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Theme(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(Tag)
    teams = models.ManyToManyField(Team)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, null = True)
    
    def __str__(self):
        return self.title

    def titular(self):
        return (self.text[:90])
