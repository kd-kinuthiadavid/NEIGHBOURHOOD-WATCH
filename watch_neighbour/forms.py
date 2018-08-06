from django import forms

from watch_neighbour.models import Profile, Neighbourhood, Post, Business, Department, Location


class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'business']



class NewNeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ['occupants_count', 'admin']


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['profile']


class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user']


class NewDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        exclude = ['user']


class NewLocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['neighbourhood', 'name']
