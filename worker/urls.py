from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name="home"),
    path('create/', views.queue_worker, name="create"),
]
