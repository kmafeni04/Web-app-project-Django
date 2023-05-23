from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from .models import Reservations
from .forms import SignUpForm
from .forms import ReservationsForm



#general logged out links
def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out"))
    return redirect('index')

def index(request):    
    return render(request, 'web_app_hotel_app/index.html')

def baseloggedout(request):
    return render(request, 'web_app_hotel_app/baseloggedout.html')

def loginselection(request):
    return render(request, 'web_app_hotel_app/loginselection.html')

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Succesful"))
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'web_app_hotel_app/guestsignup.html', {
        'form':form,
    })

def guestlogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home') 

        else:
            messages.success(request, ("Incorrect Username or Password"))
            return redirect('guestlogin')

    else:
        return render(request, 'web_app_hotel_app/guestlogin.html')

def roomssignedout(request):
    return render(request, 'web_app_hotel_app/roomssignedout.html')


#general logged in links
def base(request):
    return render(request, 'web_app_hotel_app/base.html')

def home(request):
    return render(request, 'web_app_hotel_app/home.html')

def rooms(request):
    return render(request, 'web_app_hotel_app/rooms.html')

def reservations(request):
    submitted = False
    if request.method == "POST":
        form = ReservationsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/reservations?submitted=True')
    else:
        form = ReservationsForm
        if 'submitted' in request.GET:
            submitted = True

    made_reservations = Reservations.objects.all()

    return render(request, 'web_app_hotel_app/reservations.html', {'form':form, 'submitted':submitted, 'made_reservations':made_reservations})

def services(request):
    return render(request, 'web_app_hotel_app/services.html')

def contactguest(request):
    return render(request, 'web_app_hotel_app/contactguest.html')

#admin links
def baseadmin(request):
    return render(request, 'web_app_hotel_app/baseadmin.html')

def adminlogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('admincontrol') 

        else:
            messages.success(request, ("Incorrect Username or Password"))
            return redirect('adminlogin')

    else:
        return render(request, 'web_app_hotel_app/adminlogin.html')

def admincontrol(request):
    return render(request, 'web_app_hotel_app/admincontrol.html')

def adminguestcontrol(request):
    return render(request, 'web_app_hotel_app/adminguestcontrol.html')

def roomsadmin(request):
    return render(request, 'web_app_hotel_app/roomsadmin.html')

def reservationsadmin(request):
    return render(request, 'web_app_hotel_app/reservationsadmin.html')

def contactadmin(request):
    return render(request, 'web_app_hotel_app/contactadmin.html')
