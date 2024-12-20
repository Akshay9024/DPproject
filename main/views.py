# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib.auth import logout
from django.shortcuts import redirect
import csv

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

import pandas as pd
from django.shortcuts import render

@login_required
def home_view(request):
    # Existing functionality of your home_view goes here

    # Add the CSV reading logic
    df = pd.read_csv('main/static/data/discharge_data.csv', skiprows=1, names=['datetime', 'discharge_rate'])
    df['datetime'] = pd.to_datetime(df['datetime'])
    time_series = df['datetime'].dt.strftime('%H:%M:%S').tolist()
    discharge_rate_series = df['discharge_rate'].tolist()

    # Add the new data to the context
    context = {
        'time_series': time_series,
        'discharge_rate_series': discharge_rate_series,
        # Include any other context data you already have
    }

    return render(request, 'home.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')   

