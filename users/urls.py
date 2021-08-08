from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path

from users.views import signup, profile

urlpatterns = [
    path('signup', signup, name='signup'),
    path('signin', LoginView.as_view(template_name='users/signin.html', extra_context={'title': 'Is it you?'}), name='signin'),
    path('signout', LogoutView.as_view(template_name='users/signout.html'), name='signout'),
    path('profile', profile, name='profile'),
    path('password-reset', PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset-done', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete', PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]
