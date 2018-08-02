from django.shortcuts import render

# Create your views here.
def welcome(request):
    title = 'Welcome'
    return render(request, 'welcome.html', locals())
