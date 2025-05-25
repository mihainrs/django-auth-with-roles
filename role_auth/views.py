from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from .forms import SignupForm

# Create your views here
def home(request):
    return render(request,'role_auth/home.html')

@login_required
def custom_logout(request):
    logout(request)
    return render(request, 'role_auth/logout.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'role_auth/signup.html', {'form': form})