from django.urls import path

from . import views

urlpatterns = [
    #general logged out links
    path('', views.index, name="index"),
    path('baseloggedout/', views.baseloggedout, name="baseloggedout"),
    path('loginselection/', views.loginselection, name="loginselection"),
    path('signup/', views.signup, name="signup"),
    path('guestlogin/', views.guestlogin, name="guestlogin"),
    path('roomssignedout/', views.roomssignedout, name="roomssignedout"),
    
    

    #general logged in links
    path('base/', views.base, name="base"),
    path('home/', views.home, name="home"),
    path('rooms/', views.rooms, name="rooms"),
    path('reservations/', views.reservations, name="reservations"),
    path('services/', views.services, name="services"),
    path('contactguest/', views.contactguest, name="contactguest"),

    #admin links
    path('baseadmin/', views.baseadmin, name="baseadmin"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('admincontrol/', views.admincontrol, name="admincontrol"),
    path('adminguestcontrol/', views.adminguestcontrol, name="adminguestcontrol"),
    path('roomsadmin/', views.roomsadmin, name="roomsadmin"),
    path('reservationsadmin/', views.reservationsadmin, name="reservationsadmin"),
    path('contactadmin/', views.contactadmin, name="contactadmin"),    
]

