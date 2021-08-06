from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.forms import SignUpForm, UpdateProfileForm, UpdateUserForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username}')
            return redirect('signin')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


@login_required
def profile(request):
    update_user_form = UpdateUserForm()
    update_profile_form = UpdateProfileForm()
    context = {
        'update_user_form': update_user_form,
        'update_profile_form': update_profile_form,
    }
    return render(request, 'users/profile.html', context)
