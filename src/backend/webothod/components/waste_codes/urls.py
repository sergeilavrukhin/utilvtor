from django.urls import path
from . import views

app_name = 'waste_codes'

urlpatterns = [
    path('', views.WasteCodes.as_view(), name='waste_codes_list'),
]
