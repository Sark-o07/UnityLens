from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.sign_up, name='users-sign-up'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),
         name='users-login'),
    path('log_out/', auth_views.LogoutView.as_view(template_name='users/logout.html'),
         name='users-logout'),
    path('profile/', views.profile, name='users-profile'),
    path('reset_password/', auth_views.PasswordResetView.as_view(
         template_name='users/password_reset.html',),  name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
         template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
         template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
         template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]