from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm

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

# register user
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request,user)
            messages.success(request,"You have registered successfully! Welcome")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request,'register.html',{'form':form})
