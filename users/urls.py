from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.views import signup

urlpatterns = [
    path('signup', signup, name='signup'),
    path('signin', LoginView.as_view(), name='signin'),
    path('signout', LogoutView.as_view(), name='signout'),
]
