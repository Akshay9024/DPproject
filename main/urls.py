# myapp/urls.py
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import signup_view, login_view, home_view, logout_view

urlpatterns = [
    path('', home_view, name='home'),                  # Home page
    path('signup/', signup_view, name='signup'),       # Signup page
    path('login/', login_view, name='login'),          # Login page
    path('logout', logout_view, name='logout'),      # Logout
]
