from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.fields.files import ImageField

from django.utils.regex_helper import Choice


class Profile(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='owner')
    name = models.CharField(max_length=20, null=True)

    # img = models.ImageField()


class Blog(models.Model):

    choice = (

        ('math', 'Math'),
        ('history', 'History'),
        ('technology', 'Technology')

    )

    publish_date = models.DateField(auto_now_add=True)
    publisher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='publisher')
    content = models.TextField()
    title = models.TextField()
    category = models.TextField(choices=choice, default='history')

    def __str__(self):
        return self.title
