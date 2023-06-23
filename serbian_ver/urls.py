from django.urls import path

from . import views

app_name = 'index-serbian'

urlpatterns = [
    path("", views.index, name="index-sr"),
    
]