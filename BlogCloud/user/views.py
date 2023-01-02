from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def signup(request):
    if request.method == "POST":
        fname = request.POST.get("first_name")
        lname = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(fname, lname, username, email, password)
        try:
            user = User.objects.create_user(
                first_name=fname,
                last_name=lname,
                username=username,
                email=email,
                password=password
            )
            user.save()
            messages.success(request, "Account Created Successfully. Please Login to Continue")
        except Exception as e:
            print(str(e))
            messages.error(request, "Error !!! Try with different username")

    return render(request, 'user/signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, 'user/signin.html')

def signout(request):
    logout(request)
    return redirect("home")