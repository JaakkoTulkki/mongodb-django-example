from django.db import models
import mongoengine
import datetime

# Create your models here.


class User(mongoengine.Document):
    username = mongoengine.StringField(required=True, verbose_name="Your username", max_length=50)
    created = mongoengine.DateTimeField(default=datetime.datetime.now())
