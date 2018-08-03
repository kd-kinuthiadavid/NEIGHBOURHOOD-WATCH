from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Neighbourhood(models.Model):
    neighbourhood_photo = models.ImageField(upload_to='neighbourhood/')
    neighbourhood_name = models.CharField(max_length=100, blank=True, null=True)
    neighbourhood_location = models.CharField(max_length=100, blank=True, null=True)
    occupants_count = models.IntegerField(blank=True, null=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.neighbourhood_name

class Location(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Business(models.Model):
    business_photo = models.ImageField(upload_to='business/')
    business_name = models.CharField(max_length=100, blank=True, null=True)
    business_description = models.TextField(max_length=200, blank=True, null=True)
    business_email = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.business_name

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profile/')
    name = models.CharField(max_length=100, blank=True, null=True)
    status = models.TextField(max_length=140, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(max_length=200, blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, related_name='posted_by')

    def __str__(self):
        return self.title
