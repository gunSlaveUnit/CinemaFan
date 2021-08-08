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
    return render(request, 'users/signup.html', {'title': 'Join Us Now', 'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        update_user_form = UpdateUserForm(request.POST, instance=request.user)
        update_profile_form = UpdateProfileForm(request.POST, request. FILES, instance=request.user.profile)
        if update_user_form.is_valid() and update_profile_form.is_valid():
            update_user_form.save()
            update_profile_form.save()
            messages.success(request, f'Account has been updated')
            return redirect('profile')
    else:
        update_user_form = UpdateUserForm(instance=request.user)
        update_profile_form = UpdateProfileForm(instance=request.user.profile)
    context = {
        'title': "It's you",
        'update_user_form': update_user_form,
        'update_profile_form': update_profile_form,
    }
    return render(request, 'users/profile.html', context)
