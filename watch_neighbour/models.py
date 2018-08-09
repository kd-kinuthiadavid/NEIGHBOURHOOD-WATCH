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

    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    def update_neighbourhood(self):
        self.update()

    @classmethod
    def find_neighbourhood(cls, neighbourhood_id):
        neighbourhood = cls.objects.get(neighbourhood_id=neighbourhood_id)
        return neighbourhood


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

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def update_business(self):
        self.update()

    @classmethod
    def find_business(cls, business_id):
        business = cls.objects.get(business_id=business_id)
        return business

    @classmethod
    def search_business(cls, search_term):
        businesses = cls.objects.filter(business_name__icontains=search_term)
        return businesses



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
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='posts_for')

    
    def __str__(self):
        return self.title


class Department(models.Model):
    department_photo = models.ImageField(upload_to='business/')
    department_name = models.CharField(max_length=100, blank=True, null=True)
    department_description = models.TextField(max_length=200, blank=True, null=True)
    department_email = models.CharField(max_length=100, blank=True, null=True)
    department_phone = models.IntegerField(blank=True, null=True)
    department_box = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.department_name


class Comment(models.Model):
    content = models.TextField(max_length=200, blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.content