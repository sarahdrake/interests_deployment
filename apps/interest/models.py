from __future__ import unicode_literals

from django.db import models


# Create your models here.
class InterestManager(models.Manager):
    def validate(self, postData):
        if "interest" in postData:
            if len(postData["interest"]) == 0:
                return (False,"Please enter a valid interest!")
            interest = postData['interest']
            interests = Interest.objects.filter(name=interest)
            if len(interests) == 0:
                new_interest = Interest.objects.create(name=interest)
            else:
                new_interest = interests[0]
            return (True, new_interest)
        else:
            return (False,"Please enter a valid interest!")

class Interest(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = InterestManager()



class UserManager(models.Manager):
    def validate(self, postData):
        if "name" in postData:
            if len(postData["name"]) == 0:
                return (False,"Please enter a valid name!")
            name = postData['name']
            users = User.objects.filter(name=name)
            if len(users) == 0:
                user = User.objects.create(name=name)
            else:
                user = users[0]
            return (True, user)
        else:
            return (False,"Please enter a valid name!")

class User(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    interests = models.ManyToManyField(Interest, related_name="users")
    objects = UserManager()
