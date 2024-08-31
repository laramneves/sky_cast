from django.urls import path #the path function is used to define url patterns in django
from . import views

urlpatterns = [
    path("", views.page), # returns an element for inclusion of url patterns
]
#django uses the list to determine wich view function to use