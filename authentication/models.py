from django.db import models
import mongoengine
import datetime


from django.contrib.auth.hashers import make_password


# Create your models here.


class User(mongoengine.Document):
    username = mongoengine.StringField(required=True, verbose_name="Your username", max_length=50, unique=True)
    created = mongoengine.DateTimeField(default=datetime.datetime.now())
    password = mongoengine.StringField(required=True, max_length=500)

    def save(self, force_insert=False, validate=True, clean=True,
             write_concern=None, cascade=None, cascade_kwargs=None,
             _refs=None, save_condition=None, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
        super().save(force_insert=False, validate=True, clean=True,
             write_concern=None, cascade=None, cascade_kwargs=None,
             _refs=None, save_condition=None, **kwargs)

    def create(self, **kwargs):
        super(User).create(**kwargs)
        return self

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        if validated_data.get("password"):
            instance.password = validated_data.get('password')
        instance.save()
        return instance


class Comment(mongoengine.Document):
    pass