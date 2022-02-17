from django.urls import path
from .views import getProjects

urlpatterns = [
    path('', getProjects, name='projects'),
]