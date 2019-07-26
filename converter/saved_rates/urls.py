from django.urls import path, reverse_lazy
from . import views
app_name = 'saved_rates'

urlpatterns = [
    path('saved_rates/', views.saved_rates, name='saved_rates'),
    path('db_save/', views.db_save, name='db_save'),
]