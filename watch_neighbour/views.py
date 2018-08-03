from django.shortcuts import render, redirect

# Create your views here.
from watch_neighbour.forms import NewProfileForm, NewNeighbourhoodForm, NewPostForm
from watch_neighbour.models import Neighbourhood, Profile, Post


def welcome(request):
    title = 'Welcome'

    return render(request, 'welcome.html', locals())

def all_neighbourhoods(request):
    title = 'neighbourhoods'
    neighbourhoods = Neighbourhood.objects.all()
    return render(request, 'index.html', locals())


def new_profile(request):
    current_user = request.user

    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect('neighbourhood')
    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})

def new_neighbourhood(request):
    current_user = request.user

    if request.method == 'POST':
        form = NewNeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood.user = current_user
            neighbourhood.save()
            return redirect('neighbourhood')
    else:
        form = NewNeighbourhoodForm()
    return render(request, 'new_neighbourhood.html', {"form": form})


def new_post(request):
    current_user = request.user

    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('single_neighbourhood')
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})

def current_user_profile(request, profile_id):
    profile = Profile.objects.filter(user_id=profile_id).first()
    return render(request, 'profile.html', locals())

def single_neighbourhood(request, neighbourhood_id):
    post = Post.objects.all()
    return render(request, 'single_neighbourhood.html', locals())

