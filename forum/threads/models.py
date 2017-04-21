from django.db import models

# Django provides a model for users
from django.contrib.auth.models import User

# Create your models here.

'''
This is where you store your models

Django looks specifically in this file to find your models

To apply the models to your database you must run:

    python manage.py makemigrations

then:

    python manage.py migrate

The first command creates the migrations (in the app's migrations folder)
the second command applies them to the database

'''


class Thread(models.Model):
    ''' Thread model'''

    # The title is going to be a CharField which tells the database to hold
    # the data as a string
    title = models.CharField(max_length=30)

    # A ForeignKey key almost like a pointer to another model
    author = models.ForeignKey(User, related_name="threads")
    date_posted = models.DateTimeField(auto_now_add=True)
    text = models.TextField()


class Comment(models.Model):
    '''Comment model'''
    # This author is very similar to the thread author except its for comments
    author = models.ForeignKey(User, related_name="mycomments")
    thread = models.ForeignKey(Thread, related_name="comments")
    date_posted = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
