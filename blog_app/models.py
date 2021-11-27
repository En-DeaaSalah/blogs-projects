from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.fields.files import ImageField

from django.utils.regex_helper import Choice


class Profile(models.Model):
    owner = models.OneToOneField(
        User, on_delete=models.CASCADE)
    # email = models.CharField(max_length=20, null=True)

    # old_password = models.CharField(max_length=20, null=True)

    # new_password = models.CharField(max_length=20, null=True)

    birth_date = models.DateField(null=True, blank=True)

    phone_number = models.CharField(max_length=20, blank=True, null=True)

    img = models.ImageField(null=True, default='blank-profile-picture.png')


class Blog(models.Model):

    category_choice = (

        ('math', 'Math'),
        ('history', 'History'),
        ('technology', 'Technology')

    )
    visibiliry_choice = (

        ('public', 'public'),
        ('private', 'private'),
        ('some people', 'some people')

    )

    publish_date = models.DateField(auto_now_add=True)
    publisher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='publisher')
    content = models.TextField()
    title = models.TextField()
    category = models.TextField(choices=category_choice, default='history')
    visibiliry = models.TextField(choices=visibiliry_choice, default='public')

    def __str__(self):
        return self.title
