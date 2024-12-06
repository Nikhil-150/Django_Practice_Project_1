from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),  #/challenges/
    path("<int:month>", views.monthly_challenges_number),
    path("<str:month>", views.monthly_challenges, name="month-challenge")
    # here str is to take only string dtype and if any other given it converts it in to string


]