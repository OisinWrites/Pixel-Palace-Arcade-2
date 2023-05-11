from django.urls import path
from . import views

urlpatterns = [
    path('user_profile', views.index, name='user_profile')
]
