from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=username,email=email,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/todo")
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('/signin')
    else:
        return render(request, 'signin.html',)


def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username is exists')
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email is exists')
                return redirect('/signup')
            else:
                user = User.objects.create_user(
                first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                user.save()
                return redirect('/signin')
        else:
            messages.info(request, 'password is not matching')
            return redirect('/signup')

    return render(request, 'signup.html',)

def logout(request):
    auth.logout(request)
    return redirect('/')