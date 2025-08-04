from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_habit, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password-reset/', views.password_reset_request_view, name='password_reset_request'),
    path('password-reset/done/', views.password_reset_done_view, name='password_reset_done'),
    path('password-reset/confirm/<uuid:token>/', views.password_reset_confirm_view, name='password_reset_confirm'),
    path('password-reset/complete/', views.password_reset_complete_view, name='password_reset_complete'),
]