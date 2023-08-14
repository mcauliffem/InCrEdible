from django.urls import path

from . import views

app_name = "meals"
urlpatterns = [
    path("", views.home, name="home"),
    path("<int:meal_id>/", views.detail, name="detail"),
    path("add/", views.add, name="add")
]
