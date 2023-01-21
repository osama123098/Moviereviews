from django.urls import path
from . import views

urlpatterns = [
    path('signup_account/',views.signupaccount,name='signup_account'),
    path('logout/',views.logoutaccount,name='logoutaccount'),
    path('login/',views.loginaccount,name='loginaccount'),
]
