from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def home(request):
    #checking for logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged In successfully.")
            return redirect('home')
        else:
            messages.success(request, "Error in logging In,Please Try Again")
    else:
        return render(request,'home.html',{})

#crete login 
def login_user(request):
    pass

# create logout 
def logout_user(request):
    logout(request)
    messages.success(request, "Yo have logged out successfully.")
    return redirect('home')
