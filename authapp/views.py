from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from authapp.forms import SignUpForm

# Create your views here.
#renders first parameter is a request
@login_required
def home(request):
    user = request.user
    return render(request, 'ZuriTeam/home.html', {'username': user})


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = SignUpForm(request.POST) #UserCreationForm(request.POST)#user creation form is default django form
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')#this is a dictionary
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
             form = SignUpForm() #UserCreationForm()
        return render(request, 'ZuriTeam/register.html', {'form':form})    
    else:
        form = SignUpForm() #UserCreationForm()
        return render(request, 'ZuriTeam/register.html', {'form':form})        
    
def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = UserCreationForm(request.POST)#user creation form is default django form
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')#this is a dictionary
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
             form = UserCreationForm()
        return render(request, 'ZuriTeam/index.html', {'form' : form})    
    else:
        form = UserCreationForm()
        return render(request, 'ZuriTeam/index.html', {'form' : form})        
    
def signout(request):
    logout(request)
    return redirect('signin')