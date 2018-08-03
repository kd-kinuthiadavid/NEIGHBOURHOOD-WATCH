from django import forms

from watch_neighbour.models import Profile, Neighbourhood, Post


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