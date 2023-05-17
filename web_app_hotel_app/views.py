from django.shortcuts import render
from django.http import HttpResponse


#general logged out links
def index(request):
    return render(request, 'web_app_hotel_app/index.html')

def baseloggedout(request):
    return render(request, 'web_app_hotel_app/baseloggedout.html')

def loginselection(request):
    return render(request, 'web_app_hotel_app/loginselection.html')

def signup(request):
    return render(request, 'web_app_hotel_app/guestsignup.html')

def guestlogin(request):
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
    return render(request, 'web_app_hotel_app/reservations.html')

def services(request):
    return render(request, 'web_app_hotel_app/services.html')

def contactguest(request):
    return render(request, 'web_app_hotel_app/contactguest.html')

#admin links
def baseadmin(request):
    return render(request, 'web_app_hotel_app/baseadmin.html')

def adminlogin(request):
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



