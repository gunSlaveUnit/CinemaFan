from django.contrib import messages
from django.shortcuts import render, redirect

from users.forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username}')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


def signin(request):
    pass
