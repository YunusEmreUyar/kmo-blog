from django.urls import path
from . import views


urlpatterns = [
    path('', views.homeView, name="home-blog"),
    path('owner/', views.ownerView, name="owner-blog")
]