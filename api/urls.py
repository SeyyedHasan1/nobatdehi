from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes ,name='main_api_page'),
    path('reserve/', views.get_reservers, name='reserve_api_page'),
]
