from django.urls import path

from . import views

from . import api


urlpatterns = [
    path('', views.Home, name='home'),
    path('create/', views.CreateTask, name='create_task'),
    path('api/', api.WorkerApi.as_view(), name='api'),
]
