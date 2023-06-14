from django.urls import path
from .views import vista
urlpatterns = [
    path("home/", vista, name="home")

]
