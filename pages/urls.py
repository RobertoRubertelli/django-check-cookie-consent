from django.urls import path 
from .views import Home,ReadPolicy,CheckConsentForLogin,CheckConsentForSignUp 

urlpatterns = [

    path('',Home,name='home'),

    path('readpolicy',ReadPolicy,name='readpolicy'),

    path('checkconsent',CheckConsentForLogin,name='checkconsent'),
    path('checkconsentsignup',CheckConsentForSignUp,name='checkconsentsignup'),

    
]
