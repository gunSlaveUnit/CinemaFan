from django.urls import path

from users.views import SingUp, SingIn

urlpatterns = [
    path('/signup', SignUp.as_view(), name='signup'),
    path('/signin', SignIn.as_view(), name='signin'),
]
