from django.urls import path
from . import views

app_name = 'dicts'

urlpatterns = [
    path('units/', views.Units.as_view(), name='dict_units'),
]
