from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.views import signup, profile

urlpatterns = [
    path('signup', signup, name='signup'),
    path('signin', LoginView.as_view(template_name='users/signin.html'), name='signin'),
    path('signout', LogoutView.as_view(template_name='users/signout.html'), name='signout'),
    path('profile', profile, name='profile'),
]
