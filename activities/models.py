from django.db import models

class Author(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    onsite_team = models.BooleanField() # True: onsite, False: Offshore

class Activity(models.Model):
    description = models.TextField()
    activity_type = models.CharField(max_length=200)
    author = models.ForeignKey(Author)
    ticket_number = models.IntegerField()
    hours_worked = models.IntegerField(default=0)
    created_on = models.DateTimeField()
    categorization = models.CharField(max_length=200)
