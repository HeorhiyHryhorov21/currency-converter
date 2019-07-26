from django.contrib.auth import views
from django.contrib.auth.forms import UserCreationForm
from django.urls import path, reverse_lazy
from django.views import generic
from . import views as custom_views
app_name = 'accounts'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', custom_views.signup, name='signup'),
]