
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from loginform import settings
# from django.conf import settings
# from django.core.mail import send_mail
# Create your views here.

def home(request):
    return render(request, "home.html")

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username alreay exist! please try some other username")
            return redirect('signup')

        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('signup')

        if len(username)>10:
            messages.error(request, "Usename must be 10 characters")
            return redirect('signup')
        if pass1 != pass2:
            messages.error(request, "password not matched")
            return redirect('signup')
            
        if not username.isalnum():
            messages.error(request, "username must be alpha-Numeric")
            return redirect('signup')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your Account has been successfully created!!")

        #welcome Email
# trying to verify email with gmail 
        # subject = "Welcome to our website"
        # message = "Hello!" + myuser.first_name + "!! \n" + "Welcome to our website!! \n Thank you for visiting our website \n We have also sent you a confirmmation email, please confirm your email address in order to activate your account .\n\n Thanking You\n Harsh Mishra"
        # from_email = settings.EMAIL_HOST_USER
        # to_list = [myuser.email]
        # send_mail(subject, message, from_email, to_list, fail_silently=True)

        return redirect('/signin/')

    return render(request, "signup.html")

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username , password=pass1)

        if user is not None:
            login(request, user)
            fname= user.first_name
            return render(request, "index.html", {'fname':fname})

        else:
            messages.error(request, "Bad data")
            return redirect('home')
    return render(request, "signin.html")

def signout(request):
    logout(request)
    messages.success(request, "logged out successfully!!")
    return redirect('home')


def one(request):
    return render(request, '1/one.html')

def two(request):
    return render(request, '2/two.html')

def three(request):
    return render(request, '3/three.html')

def four(request):
    return render(request, '4/four.html')

def five(request):
    return render(request, '5/five.html')

def six(request):
    return render(request, '6/six.html')

def seven(request):
    return render(request, '7/seven.html')

def eight(request):
    return render(request, '8/eight.html')

def index(request):
    return render(request, 'index.html')